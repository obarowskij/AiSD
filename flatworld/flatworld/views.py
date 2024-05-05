from .models import Adventure
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from io import BytesIO
from django.core.files import File
from django.conf import settings
import os
import time

from .functions.calculate_hull import calculate_hull
from .functions.factory import generate_factory
from .functions.bearers import generate_bearers
from .functions.fence import visualize_fence
from .functions.generate_song import generate_song


class IndexView(TemplateView):
    def get(self, request):
        adventure_exists = Adventure.objects.filter(id=1).exists()
        print(adventure_exists)
        return render(
            request,
            "flatworld/index.html",
            {"adventure_exists": adventure_exists},
        )

class ContinueView(View):
    def get(self, request):
        try:
            adventure = Adventure.objects.get(id=1)
        except Adventure.DoesNotExist:
            return render(request, "flatworld/error.html")
        if not adventure.bearers or not adventure.factory:
            return FactoryView.get(self, request)
        if not adventure.fence:
            return FenceView.get(self, request)
        return FenceView.get(self, request)


class ResetView(APIView):
    def post(self, request):
        try:
            adventure = Adventure.objects.get(id=1)

            adventure.world.delete()
            adventure.world = None
            adventure.save()
            adventure.delete()
            return Response({"message": "Adventure has been reset."})
        except Adventure.DoesNotExist:
            return Response({"message": "No adventure to reset."})

    def get(self, request):
        adventure_exists = Adventure.objects.filter(id=1).exists()
        return Response({"adventure_exists": adventure_exists})

    def get_plot_path(self, filename):
        return os.path.join(settings.MEDIA_ROOT, "images", filename)


class GenerateWorldView(APIView):
    def get(self, request):
        try:
            adventure = Adventure.objects.get(id=1)
            return render(
                request,
                "flatworld/world.html",
                {
                    "world_exists": True,
                    "world": adventure.world,
                    "world_points": int(adventure.world_points),
                    "hull_points": len(adventure.hull_points) - 1,
                },
            )
        except Adventure.DoesNotExist:
            return render(
                request, "flatworld/world.html", {"world_exists": False}
            )

    def post(self, request):
        world_points = request.data.get("inputPoints")
        if not world_points:
            return Response({"error": "inputPoints is required"}, status=400)
        try:
            world_points = int(world_points)
        except ValueError:
            return Response(
                {"error": "inputPoints must be an integer"}, status=400
            )

        # image_data, world_points, hull_points = calculate_hull(input_points)
        image_data, hull_points = calculate_hull(world_points)
        hull = BytesIO(image_data)
        hull.seek(0)
        # world_points = [list(point) for point in world_points]
        hull_points = [list(point) for point in hull_points]

        adventure, created = Adventure.objects.get_or_create(
            id=1,
            defaults={
                "world_points": world_points,
                "hull_points": hull_points,
            },
        )
        if not created:
            adventure.world_points = world_points
            adventure.hull_points = hull_points
            adventure.save()

        with open("temp.png", "wb") as f:
            f.write(hull.read())
        filename = "plot_{}.png".format(int(time.time()))
        with open("temp.png", "rb") as f:
            adventure.world.save(filename, File(f))
        os.remove("temp.png")
        world_url = adventure.world.url
        return JsonResponse({"world_url": world_url})


class FactoryView(APIView):
    def get(self, request):
        try:
            adventure = Adventure.objects.get(id=1)
            # if not adventure.song:
                # return render(request, "flatworld/error.html")
            return render(
                request,
                "flatworld/bearersAndFactory.html",
                {
                    "factory_exists": adventure.factory,
                    "bearers_exists": adventure.bearers,
                    "factory": adventure.factory,
                    "bearers": adventure.bearers,
                },
            )
        except Adventure.DoesNotExist:
            return render(request, "flatworld/error.html")

    def post(self, request):
        adventure = Adventure.objects.get(id=1)
        hull_points = adventure.hull_points
        factory = generate_factory(hull_points)
        adventure.factory = [factory.x, factory.y]
        adventure.save()
        print(factory)
        return JsonResponse({"factory": [factory.x, factory.y]})


class BearersView(APIView):
    def post(self, request):
        inputPoints = request.data.get("inputPoints")
        if not inputPoints:
            return Response({"error": "inputPoints is required"}, status=400)
        try:
            inputPoints = int(inputPoints)
        except ValueError:
            return Response(
                {"error": "inputPoints must be an integer"}, status=400
            )
        adventure = Adventure.objects.get(id=1)
        pairs, people = generate_bearers(inputPoints)
        people = [person.to_dict() for person in people]

        adventure.bearers = pairs
        adventure.inhabitants = people
        adventure.save()
        return JsonResponse({"pairs": pairs})


class FenceView(APIView):
    def get(self, request):
        try:
            adventure = Adventure.objects.get(id=1)
            if "fence" in request.GET:
                hull_points = adventure.hull_points
                factory = adventure.factory
                world_points = adventure.world_points

                image_data = visualize_fence(hull_points, world_points, factory)
                image_data.seek(0)
                with open("temp.png", "wb") as f:
                    f.write(image_data.read())
                filename = "fence_{}.png".format(int(time.time()))
                with open("temp.png", "rb") as f:
                    adventure.fence.save(filename, File(f))
                os.remove("temp.png")
                fence_url = adventure.fence.url
                return JsonResponse({"fence_url": fence_url})
            else:
                if not adventure.bearers and not adventure.factory:
                    return render(request, "flatworld/error.html")
                return render(
                    request,
                    "flatworld/fence.html",
                    {"fence_cost": adventure.fence_cost},
                )
        except Adventure.DoesNotExist:
            return render(request, "flatworld/error.html")
        
    def post(self, request):
        pass


class SongView(APIView):
    def get(self, request):
        try:
            adventure = Adventure.objects.get(id=1)
            if not adventure.song:
                song = generate_song()
                adventure.song = song
                adventure.save()
            song_words = adventure.song.split()
            return render(
                request,
                "flatworld/song.html",
                {
                    "changed_song_exists": adventure.changed_song,
                    "song_words": song_words,
                },
            )
        except Adventure.DoesNotExist:
            return render(request, "flatworld/error.html")


class GuardsView(APIView):
    def get(self, request):
        return render(request, "flatworld/guards.html")
