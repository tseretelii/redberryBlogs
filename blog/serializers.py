from rest_framework import serializers
from .models import Blog, Category
from django.contrib.auth import get_user_model
from rest_framework import serializers

class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        email = data.get('email')

        if email:
            user_model = get_user_model()
            try:
                user = user_model.objects.get(email=email, is_active=True)
            except user_model.DoesNotExist:
                msg = 'User with this email does not exist or is inactive.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email".'
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'publish_date', 'categories', 'email', 'author']

    def create(self, validated_data):
        category_ids = self.context['request'].data.get('categories', [])
        blog = Blog.objects.create(**validated_data)
        category_ids = [int(cid) for cid in category_ids]
        if category_ids:
            blog.categories.set(category_ids)

        return blog

# class BlogSerializer(serializers.ModelSerializer):
#     categories = serializers.PrimaryKeyRelatedField(many = True, queryset = Category.objects.all(), write_only = True)
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'description','image', 'publish_date', 'categories', 'email','author']
#     def create(self,validated_data):
#         categories_data = validated_data.pop('categories')
#         blog = Blog.objects.create(**validated_data)
#         blog.categories.set(categories_data)
#         return blog
