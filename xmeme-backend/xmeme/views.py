from django.http import JsonResponse
from xmeme.models import MemePost, HashTags
from xmeme.serializers import memePostSerializer, hashTagsPostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MemePostAll(APIView):

    # To get top 100 memes available with latest posted first
    def get(self, request):
        posts = MemePost.objects.all().order_by('-id')[:100]
        memeSerializer = memePostSerializer(posts, many=True)
        return JsonResponse(memeSerializer.data, safe=False, status=status.HTTP_200_OK)

    # To add new meme post to database
    def post(self, request):
        serializer = memePostSerializer(data=request.data)
        all_words = request.data["caption"].split(" ")

        all_tags = []
        for i in all_words:
            if i.startswith("#"):
                all_tags.append(i)

        if serializer.is_valid():
            serializer.save()
            post = MemePost.objects.get(id=serializer.data["id"])
            ht = HashTags()
            ht.tags = "".join(all_tags)
            ht.post = post
            ht.save()
            return Response({"id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemePostSingle(APIView):

    # To get the single meme post
    def get(self, request, id):
        try:
            posts = MemePost.objects.get(id=id)
            serializer = memePostSerializer(posts)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except MemePost.DoesNotExist:
            return JsonResponse({"error": "The requested resource cannot be found."}, safe=False, status=status.HTTP_404_NOT_FOUND)

    # To update the existing post without changing name, only url and caption are allowed
    def patch(self, request, id):
        try:
            posts = MemePost.objects.get(id=id)
            del request.data["name"]
            print(request.data)
            serializer = memePostSerializer(
                posts, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(status=status.HTTP_200_OK)
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
        except MemePost.DoesNotExist:
            return JsonResponse({"error": "The requested resource cannot be found."}, safe=False, status=status.HTTP_404_NOT_FOUND)


class HashTag(APIView):

    # To fetch all the posts having same hashtags
    def get(self, request, tagName):
        all_posts = HashTags.objects.filter(
            tags__icontains=tagName).order_by('-post')
        posts = []
        for i in all_posts:
            posts.append({"id": i.post.id, "name": i.post.name,
                          "caption": i.post.caption, "url": i.post.url})
        return JsonResponse(posts, safe=False, status=status.HTTP_200_OK)


class memeCount(APIView):

    # To get the current count of the memes present in the database
    def get(self, request):
        memeCount = MemePost.objects.all()
        return JsonResponse({"length": len(memeCount)}, safe=False, status=status.HTTP_200_OK)
