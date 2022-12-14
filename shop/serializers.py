from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField("get_image_params")

    class Meta:
        model = Product
        fields = ["title", "barcode", "price", "status", "image"]

    def get_image_params(self, obj) -> dict:
        path, extension = obj.image.path.rsplit(".", 1)
        image_formats = [extension, "webp"]
        return {"path": path, "formats": image_formats}
