from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.validators import ValidationError
from .serializers import CartItemSerializer
from .models import CartItem
from store.models import Product

# Create your views here.

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        session_key = self.request.session.session_key

        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        product_id = self.request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        image = product.images.first()

        if not image:
            raise ValidationError("No image found for the selected product.")
        
        serializer.save(session_key= session_key, product= product, image= image)

