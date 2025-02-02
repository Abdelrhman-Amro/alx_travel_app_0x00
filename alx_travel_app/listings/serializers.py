from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source="host.username", read_only=True)
    average_rating = serializers.SerializerMethodField()
