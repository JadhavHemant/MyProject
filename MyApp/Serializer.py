from rest_framework import serializers
from MyApp.models import *

# ---------------------------Topics Serializer ------------------------

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopicsModel
        fields=['topic_name','flag']

# ---------------------------Content Serializer ------------------------

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentModel
        fields=['content_name','topic_id','flag']

# ---------------------------Postcategories Serializer ------------------------

class PostcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postcategories
        fields=['category_name','flag']
        
# ---------------------------States Serializer ------------------------

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatesModel
        fields=['state_Name','flag']     

# ---------------------------States Serializer ------------------------

class CitysSerializer(serializers.ModelSerializer):
    class Meta:
        model=CitysModel
        fields=['city_name','state_id','flag']   
        
        
        
# ---------------------------Locations Serializer ------------------------

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=LocationModel
        fields=['location_name','city_id','flag']   

# ---------------------------Qualifications Serializer ------------------------

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=QualificationModel
        fields=['qualification','flag'] 
        
        
 
# ---------------------------Specializations Serializer ------------------------

class SpecializationsnSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpecializationModel
        fields=['specialization','qualification_id','flag'] 
  
               
# ---------------------------Roles Serializer ------------------------

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoleModel
        fields=['role','flag'] 
        
               
# ---------------------------Genders Serializer ------------------------

class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model=GenderModel
        fields=['gender','flag'] 
                               
        
# ---------------------------Designations Serializer ------------------------

class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model=DesignationModel
        fields=['designation','flag'] 
                               
                 
# ---------------------------UserDetails Serializer ------------------------

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetailsModel
        fields=['first_name','last_name','gender_id','location_id','local_address','role_id','birth_date','joining_date','user_photo','mobile_number','emial_address','user_name','is_premium','password','flag'] 
                               
                  
# ---------------------------UserQualification Serializer ------------------------

class QualiSerializer(serializers.ModelSerializer):
    class Meta:
        model=QualiModel
        fields=['user_id','specialization_id','university','passing_year','medium','percentage','flag'] 
                 
# ---------------------------experience_details Serializer ------------------------

class ExperianceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExperianceDetailsModel
        fields=['user_id','designation_id','company_name','from_year','to_year','job_descrption','flag']         
        
# ---------------------------user_professional_expertise Serializer ------------------------

class UserProfessionalExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfessionalExpertiseModel
        fields=['user_id','specilization_id','description','flag']       
        
# ---------------------------user_posts Serializer ------------------------

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPostModel
        fields=['user_id','post_date','post_title','post_description','photo','is_active','flag']       
        

# ---------------------------post_comments Serializer ------------------------

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostCommentsModel
        fields=['post_id','comment_date','comment_by_user','comment_message','comment_photo','flag']         
        
        
# ---------------------------post_comment_replys Serializer ------------------------

class PostCommentReplysSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostCommentReplymodel
        fields=['comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag'] 
 
 
 # ---------------------------post_likes_dislikes Serializer ------------------------

class PostLikesDislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLikesDislikesModel
        fields=['post_id','like_dislike_date','like_dislike_by_user','is_like','flag']
        
        
# ---------------------------post_likes_shares Serializer ------------------------

class PostLikesSharesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLikesSharesModel
        fields=['post_id','share_date','share_by_user','flag']
      
      
        
# ---------------------------Admin_Details Serializer ------------------------

class AdminDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminDetails
        fields=['user_name','password']
        
               
# ---------------------------CodePost Serializer ------------------------

class CodePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodePostModel
        fields=['user_id','date','content_id','question','code','description','is_active','flag']
        
        
# ---------------------------tbpost_comments Serializer ------------------------

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostComment
        fields=['post_id','comment_date','comment_by_user','comment_message','comment_photo','flag']
        
# ---------------------------Genders Serializer ------------------------

class PostCommentReplysSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostCommentReplys
        fields=['comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag']
                 
# ---------------------------tbpost_likes_dislikes Serializer ------------------------

class PostLikesDislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLikesDislikesTBModel
        fields=['post_id','like_dislike_date','like_dislike_by_user','is_like','flag'] 

        
# ---------------------------tblpost_likes_shares Serializer ------------------------

class LikesSharesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=LikesSharesPostModel
        fields=['post_id','share_date','share_by_user','flag']
          
          
                
# ---------------------------JobOpenings Serializer ------------------------

class JobOpeningslSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobOpeningsModel
        fields=['opening_date','opening_by','company_name','job_title','experience_required','job_description','is_active','flag']
                                
# ---------------------------post_comments Serializer ------------------------

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentPostModel
        fields=['opening_id','comment_date','comment_by_user','comment_message','comment_photo','flag']
        

# ---------------------------post_comment_replys Serializer ------------------------

class CommentPostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentPostReplyModel
        fields=['comment_id','reply_date','reply_by_user','reply_mesage','comment_photo','flag']


# ---------------------------post_likes_dislikes Serializer ------------------------

class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostDislikeModel
        fields=['opening_id','like_dislike_date','like_dislike_by_user','is_like','flag']  
       
       
# ---------------------------lpost_likes_shares Serializer ------------------------

class PostLikesSharesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLikesSharesTableModel
        fields=['opening_id','share_date','share_by_user','flag']       
       
 

# ---------------------------updates Serializer ------------------------

class UpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UpdateModel
        fields=['update_date','update_title','update_desription','flag']
        
        
        
               
        
        
        
        
        
        
        
        
        
    