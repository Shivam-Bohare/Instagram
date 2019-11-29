from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#from django.contrib.auth.models import AbstractUser

# -----------------------------------User Profile Model Class---------------------------------#
class Profile(models.Model):
    """Model for user info to be displayed on the website"""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)
    
    website = models.CharField(
        verbose_name="Website", max_length=20, blank=True, null=True
    )
    
    gender = models.CharField(
        verbose_name="Gender", blank=True, null=True, max_length=10
    )

    privacy = models.BooleanField(verbose_name="Privacy", default=False, null=True)
    
    profile_picture = models.ImageField(blank=True, null=True, upload_to='images/')
    
    time = models.DateTimeField(verbose_name="User Creation Time", auto_now=True, null=True)
    
    COUNTRY_CODES = (
        ("591", "Bolivia (+591)"),
        ("387", "Bosnia Herzegovina (+387)"),
        ("267", "Botswana (+267)"),
        ("55", "Brazil (+55)"),
        ("673", "Brunei (+673)"),
        ("359", "Bulgaria (+359)"),
        ("226", "Burkina Faso (+226)"),
        ("257", "Burundi (+257)"),
        ("855", "Cambodia (+855)"),
        ("237", "Cameroon (+237)"),
        ("1", "Canada (+1)"),
        ("238", "Cape Verde Islands (+238)"),
        ("1345", "Cayman Islands (+1345)"),
        ("236", "Central Afri   can Republic (+236)"),
        ("56", "Chile (+56)"),
        ("86", "China (+86)"),
        ("57", "Colombia (+57)"),
        ("269", "Comoros (+269)"),
        ("242", "Congo (+242)"),
        ("682", "Cook Islands (+682)"),
        ("506", "Costa Rica (+506)"),
        ("385", "Croatia (+385)"),
        ("53", "Cuba (+53)"),
        ("90392", "Cyprus North (+90392)"),
        ("357", "Cyprus South (+357)"),
        ("42", "Czech Republic (+42)"),
        ("45", "Denmark (+45)"),
        ("253", "Djibouti (+253)"),
        ("1809", "Dominica (+1809)"),
        ("1809", "Dominican Republic (+1809)"),
        ("593", "Ecuador (+593)"),
        ("20", "Egypt (+20)"),
        ("503", "El Salvador (+503)"),
        ("240", "Equatorial Guinea (+240)"),
        ("291", "Eritrea (+291)"),
        ("372", "Estonia (+372)"),
        ("251", "Ethiopia (+251)"),
        ("500", "Falkland Islands (+500)"),
        ("298", "Faroe Islands (+298)"),
        ("679", "Fiji (+679)"),
        ("358", "Finland (+358)"),
        ("33", "France (+33)"),
        ("594", "French Guiana (+594)"),
        ("689", "French Polynesia (+689)"),
        ("241", "Gabon (+241)"),
        ("220", "Gambia (+220)"),
        ("7880", "Georgia (+7880)"),
        ("49", "Germany (+49)"),
        ("233", "Ghana (+233)"),
        ("350", "Gibraltar (+350)"),
        ("30", "Greece (+30)"),
        ("299", "Greenland (+299)"),
        ("1473", "Grenada (+1473)"),
        ("590", "Guadeloupe (+590)"),
        ("671", "Guam (+671)"),
        ("502", "Guatemala (+502)"),
        ("224", "Guinea (+224)"),
        ("245", "Guinea - Bissau (+245)"),
        ("592", "Guyana (+592)"),
        ("509", "Haiti (+509)"),
        ("504", "Honduras (+504)"),
        ("852", "Hong Kong (+852)"),
        ("36", "Hungary (+36)"),
        ("354", "Iceland (+354)"),
        ("91", "India (+91)"),
        ("62", "Indonesia (+62)"),
        ("98", "Iran (+98)"),
        ("964", "Iraq (+964)"),
        ("353", "Ireland (+353)"),
        ("972", "Israel (+972)"),
        ("39", "Italy (+39)"),
        ("1876", "Jamaica (+1876)"),
        ("81", "Japan (+81)"),
        ("962", "Jordan (+962)"),
        ("7", "Kazakhstan (+7)"),
        ("254", "Kenya (+254)"),
        ("686", "Kiribati (+686)"),
        ("850", "Korea North (+850)"),
        ("82", "Korea South (+82)"),
        ("965", "Kuwait (+965)"),
        ("996", "Kyrgyzstan (+996)"),
        ("856", "Laos (+856)"),
        ("371", "Latvia (+371)"),
        ("961", "Lebanon (+961)"),
        ("266", "Lesotho (+266)"),
        ("231", "Liberia (+231)"),
        ("218", "Libya (+218)"),
        ("417", "Liechtenstein (+417)"),
        ("370", "Lithuania (+370)"),
        ("352", "Luxembourg (+352)"),
        ("853", "Macao (+853)"),
        ("389", "Macedonia (+389)"),
        ("261", "Madagascar (+261)"),
        ("265", "Malawi (+265)"),
        ("60", "Malaysia (+60)"),
        ("960", "Maldives (+960)"),
        ("223", "Mali (+223)"),
        ("356", "Malta (+356)"),
        ("692", "Marshall Islands (+692)"),
        ("596", "Martinique (+596)"),
        ("222", "Mauritania (+222)"),
        ("269", "Mayotte (+269)"),
        ("52", "Mexico (+52)"),
        ("691", "Micronesia (+691)"),
        ("373", "Moldova (+373)"),
        ("377", "Monaco (+377)"),
        ("976", "Mongolia (+976)"),
        ("1664", "Montserrat (+1664)"),
        ("212", "Morocco (+212)"),
        ("258", "Mozambique (+258)"),
        ("95", "Myanmar (+95)"),
        ("264", "Namibia (+264)"),
        ("674", "Nauru (+674)"),
        ("977", "Nepal (+977)"),
        ("31", "Netherlands (+31)"),
        ("687", "New Caledonia (+687)"),
        ("64", "New Zealand (+64)"),
        ("505", "Nicaragua (+505)"),
        ("227", "Niger (+227)"),
        ("234", "Nigeria (+234)"),
        ("683", "Niue (+683)"),
        ("672", "Norfolk Islands (+672)"),
        ("670", "Northern Marianas (+670)"),
        ("47", "Norway (+47)"),
        ("968", "Oman (+968)"),
        ("680", "Palau (+680)"),
        ("507", "Panama (+507)"),
        ("675", "Papua New Guinea (+675)"),
        ("595", "Paraguay (+595)"),
        ("51", "Peru (+51)"),
        ("63", "Philippines (+63)"),
        ("48", "Poland (+48)"),
        ("351", "Portugal (+351)"),
        ("1787", "Puerto Rico (+1787)"),
        ("974", "Qatar (+974)"),
        ("262", "Reunion (+262)"),
        ("40", "Romania (+40)"),
        ("7", "Russia (+7)"),
        ("250", "Rwanda (+250)"),
        ("378", "San Marino (+378)"),
        ("239", "Sao Tome & Principe (+239)"),
        ("966", "Saudi Arabia (+966)"),
        ("221", "Senegal (+221)"),
        ("381", "Serbia (+381)"),
        ("248", "Seychelles (+248)"),
        ("232", "Sierra Leone (+232)"),
        ("65", "Singapore (+65)"),
        ("421", "Slovak Republic (+421)"),
        ("386", "Slovenia (+386)"),
        ("677", "Solomon Islands (+677)"),
        ("252", "Somalia (+252)"),
        ("27", "South Africa (+27)"),
        ("34", "Spain (+34)"),
        ("94", "Sri Lanka (+94)"),
        ("290", "St. Helena (+290)"),
        ("1869", "St. Kitts (+1869)"),
        ("1758", "St. Lucia (+1758)"),
        ("249", "Sudan (+249)"),
        ("597", "Suriname (+597)"),
        ("268", "Swaziland (+268)"),
        ("46", "Sweden (+46)"),
        ("41", "Switzerland (+41)"),
        ("963", "Syria (+963)"),
        ("886", "Taiwan (+886)"),
        ("7", "Tajikstan (+7)"),
        ("66", "Thailand (+66)"),
        ("228", "Togo (+228)"),
        ("676", "Tonga (+676)"),
        ("1868", "Trinidad & Tobago (+1868)"),
        ("216", "Tunisia (+216)"),
        ("90", "Turkey (+90)"),
        ("7", "Turkmenistan (+7)"),
        ("993", "Turkmenistan (+993)"),
        ("1649", "Turks & Caicos Islands (+1649)"),
        ("688", "Tuvalu (+688)"),
        ("256", "Uganda (+256)"),
        ("380", "Ukraine (+380)"),
        ("971", "United Arab Emirates (+971)"),
        ("598", "Uruguay (+598)"),
        ("7", "Uzbekistan (+7)"),
        ("678", "Vanuatu (+678)"),
        ("379", "Vatican City (+379)"),
        ("58", "Venezuela (+58)"),
        ("84", "Vietnam (+84)"),
        ("84", "Virgin Islands - British (+1284)"),
        ("84", "Virgin Islands - US (+1340)"),
        ("681", "Wallis & Futuna (+681)"),
        ("969", "Yemen (North)(+969)"),
        ("967", "Yemen (South)(+967)"),
        ("260", "Zambia (+260)"),
        ("263", "Zimbabwe (+263)"),
    )

    phone_country_code = models.CharField(
        verbose_name="Country Code", choices=COUNTRY_CODES, default="91", max_length=5, null=True, blank = True
    )
    phone_number = models.IntegerField(verbose_name="Phone Number", unique=True , null=True, blank=True)

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.user_id.username}"  # pylint: disable=no-member
    
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance) # pylint: disable=no-member

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs): # pylint: disable=no-self-argument
    #     instance.profile.save()

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of UserInfo."""
    #     return reverse('userinfo-detail-view', args=[str(self.id)]) # pylint: disable=no-member

# -----------------------------------Picture Model Class---------------------------------#
class Picture(models.Model):
    picture_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="Upload Time", auto_now=True)
    picture_description = models.TextField(verbose_name="Picture Description" , blank=True, null=True)
    picture = models.ImageField(null = True, upload_to='images/')
    
    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.picture}" # pylint: disable=no-member


# -----------------------------------Comment Model Class---------------------------------#
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_id = models.ForeignKey(Picture, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Comment Description")
    time = models.DateTimeField(verbose_name="Comment Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member


# -----------------------------------Comment Reply Model Class---------------------------------#
class CommentReply(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Reply Description")
    time = models.DateTimeField(verbose_name="Reply Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member


# -----------------------------------Picture Like Model Class---------------------------------#
class PictureLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_id = models.ForeignKey(Picture, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="Picture Like Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member


# -----------------------------------Follow Model Class---------------------------------#
class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    follow_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed"
    )
    time = models.DateTimeField(verbose_name="Follow Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member


# -----------------------------------Follow Request Model Class---------------------------------#
class FollowRequest(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requester"
    )
    request_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="approver"
    )
    time = models.DateTimeField(verbose_name="Follow Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member


# -----------------------------------Block Model Class---------------------------------#
class Block(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocker")
    block_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blocked"
    )
    time = models.DateTimeField(verbose_name="Follow Time", auto_now=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id}"  # pylint: disable=no-member

