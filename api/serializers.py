import json, time
from rest_framework import serializers
from api.models import ContentHTML, Images, FileUpload

class ContentHTMLSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentHTML
        fields = ('id',
                  'created',  
                  'uuid',
                  'page',
                  'regions',
                  'images')

    def to_representation(self, instance):
        ret = super(ContentHTMLSerializer, self).to_representation(instance)
        ret['regions'] = json.loads(ret['regions'])
        return ret

    def validate(self, data):
        return data

class ImagesSerializer(serializers.ModelSerializer):

    size = serializers.ListField(
        read_only=True,
        child=serializers.IntegerField()
    )

    class Meta:
        model = Images
        fields = ('id',
                  'created',
                  'image',
                  'name',
                  'size',

                  'edited_width',
                  'edited_crop',
                  'edited_direction',
                  )


    def to_representation(self, instance):
        ret = super(ImagesSerializer, self).to_representation(instance)
        if ret['image']:
            
            # Modify the image URL by adding an _ignore param
            # This will force the browser to reload the image

            ret['image'] = "%s?_ignore=%s" % (ret['image'], time.time())
        return ret