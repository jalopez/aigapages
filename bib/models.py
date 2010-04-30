# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models




class Publication(models.Model):
    pub_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    year = models.CharField(max_length=381)
    actualyear = models.CharField(max_length=381)
    title = models.TextField()
    bibtex_id = models.CharField(max_length=765)
    report_type = models.CharField(max_length=765)
    pub_type = models.CharField(max_length=39, blank=True)
    survey = models.IntegerField()
    mark = models.IntegerField()
    series = models.CharField(max_length=381)
    volume = models.CharField(max_length=381)
    publisher = models.CharField(max_length=381)
    location = models.CharField(max_length=381)
    issn = models.CharField(max_length=96)
    isbn = models.CharField(max_length=96)
    firstpage = models.CharField(max_length=30)
    lastpage = models.CharField(max_length=30)
    journal = models.CharField(max_length=765)
    booktitle = models.CharField(max_length=765)
    number = models.CharField(max_length=765)
    institution = models.CharField(max_length=765)
    address = models.CharField(max_length=765)
    chapter = models.CharField(max_length=381)
    edition = models.CharField(max_length=765)
    howpublished = models.CharField(max_length=765)
    month = models.CharField(max_length=765)
    organization = models.CharField(max_length=765)
    school = models.CharField(max_length=765)
    note = models.TextField()
    abstract = models.TextField()
    url = models.CharField(max_length=765)
    doi = models.CharField(max_length=765)
    crossref = models.CharField(max_length=765)
    namekey = models.CharField(max_length=765)
    userfields = models.TextField()
    specialchars = models.CharField(max_length=15)
    cleanjournal = models.CharField(max_length=765)
    cleantitle = models.CharField(max_length=765)
    read_access_level = models.CharField(max_length=21)
    edit_access_level = models.CharField(max_length=21)
    group_id = models.IntegerField()
    derived_read_access_level = models.CharField(max_length=21)
    derived_edit_access_level = models.CharField(max_length=21)
    cleanauthor = models.TextField(blank=True)
    pages = models.CharField(max_length=765)
    #authors = models.ManyToManyField(Author, through='Publicationauthorlink')
    class Meta:
        db_table = u'publication'

    def author_list(self):
        return self.author_set.order_by('publicationauthorlink__rank')


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=765)
    von = models.CharField(max_length=765)
    firstname = models.CharField(max_length=765)
    email = models.CharField(max_length=765)
    url = models.CharField(max_length=765)
    institute = models.CharField(max_length=765)
    specialchars = models.CharField(max_length=15)
    cleanname = models.CharField(max_length=765)
    jr = models.CharField(max_length=765, blank=True)
    publications = models.ManyToManyField(Publication, through='Publicationauthorlink')
    class Meta:
        db_table = u'author'

class Publicationauthorlink(models.Model):
    pub = models.ForeignKey(Publication)
    author = models.ForeignKey(Author)
    rank = models.IntegerField()
    is_editor = models.CharField(max_length=3, primary_key=True)
    class Meta:
        db_table = u'publicationauthorlink'


# THIS IS SPARTAAAAA
#
#
#class Attachments(models.Model):
#    pub_id = models.IntegerField()
#    location = models.CharField(max_length=765)
#    note = models.CharField(max_length=765)
#    ismain = models.CharField(max_length=15)
#    user_id = models.IntegerField()
#    mime = models.CharField(max_length=300)
#    name = models.CharField(max_length=765)
#    isremote = models.CharField(max_length=15)
#    att_id = models.IntegerField(primary_key=True)
#    read_access_level = models.CharField(max_length=21)
#    edit_access_level = models.CharField(max_length=21)
#    group_id = models.IntegerField()
#    derived_read_access_level = models.CharField(max_length=21)
#    derived_edit_access_level = models.CharField(max_length=21)
#    class Meta:
#        db_table = u'attachments'
#
#
#class Availablerights(models.Model):
#    name = models.CharField(max_length=60, primary_key=True)
#    description = models.CharField(max_length=765)
#    class Meta:
#        db_table = u'availablerights'
#
#class Changehistory(models.Model):
#    version = models.CharField(max_length=60, primary_key=True)
#    type = models.CharField(max_length=150)
#    description = models.TextField()
#    class Meta:
#        db_table = u'changehistory'
#
#class Config(models.Model):
#    setting = models.CharField(max_length=765, primary_key=True)
#    value = models.TextField()
#    class Meta:
#        db_table = u'config'
#
#class Grouprightsprofilelink(models.Model):
#    group_id = models.IntegerField(primary_key=True)
#    rightsprofile_id = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = u'grouprightsprofilelink'
#
#class Keywords(models.Model):
#    keyword_id = models.IntegerField(primary_key=True)
#    keyword = models.TextField()
#    cleankeyword = models.TextField()
#    class Meta:
#        db_table = u'keywords'
#
#class Logintegration(models.Model):
#    token = models.CharField(max_length=90, primary_key=True)
#    time = models.IntegerField()
#    serial = models.IntegerField()
#    keepchecking = models.CharField(max_length=15)
#    status = models.CharField(max_length=27)
#    sitename = models.CharField(max_length=765)
#    class Meta:
#        db_table = u'logintegration'
#
#class Notecrossrefid(models.Model):
#    note_id = models.IntegerField()
#    xref_id = models.IntegerField()
#    class Meta:
#        db_table = u'notecrossrefid'
#
#class Notes(models.Model):
#    note_id = models.IntegerField(primary_key=True)
#    pub_id = models.IntegerField()
#    user_id = models.IntegerField()
#    rights = models.CharField(max_length=21)
#    text = models.TextField(blank=True)
#    read_access_level = models.CharField(max_length=21)
#    edit_access_level = models.CharField(max_length=21)
#    group_id = models.IntegerField()
#    derived_read_access_level = models.CharField(max_length=21)
#    derived_edit_access_level = models.CharField(max_length=21)
#    class Meta:
#        db_table = u'notes'
#
#
#
#class Publicationkeywordlink(models.Model):
#    pub_id = models.IntegerField(primary_key=True)
#    keyword_id = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = u'publicationkeywordlink'
#
#class Rightsprofilerightlink(models.Model):
#    rightsprofile_id = models.IntegerField(primary_key=True)
#    right_name = models.CharField(max_length=60, primary_key=True)
#    class Meta:
#        db_table = u'rightsprofilerightlink'
#
#class Rightsprofiles(models.Model):
#    rightsprofile_id = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=60)
#    class Meta:
#        db_table = u'rightsprofiles'
#
#class Topicpublicationlink(models.Model):
#    topic_id = models.IntegerField(primary_key=True)
#    pub_id = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = u'topicpublicationlink'
#
#class Topics(models.Model):
#    topic_id = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=765, blank=True)
#    description = models.TextField(blank=True)
#    url = models.CharField(max_length=765)
#    user_id = models.IntegerField()
#    read_access_level = models.CharField(max_length=21)
#    edit_access_level = models.CharField(max_length=21)
#    group_id = models.IntegerField()
#    derived_read_access_level = models.CharField(max_length=21)
#    derived_edit_access_level = models.CharField(max_length=21)
#    cleanname = models.CharField(max_length=765, blank=True)
#    class Meta:
#        db_table = u'topics'
#
#class Topictopiclink(models.Model):
#    source_topic_id = models.IntegerField(primary_key=True)
#    target_topic_id = models.IntegerField()
#    class Meta:
#        db_table = u'topictopiclink'
#
#class Userbookmarklists(models.Model):
#    user_id = models.IntegerField(primary_key=True)
#    pub_id = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = u'userbookmarklists'
#
#class Usergrouplink(models.Model):
#    user_id = models.IntegerField(primary_key=True)
#    group_id = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = u'usergrouplink'
#
#class Userpublicationmark(models.Model):
#    pub_id = models.IntegerField(primary_key=True)
#    user_id = models.IntegerField(primary_key=True)
#    mark = models.CharField(max_length=3)
#    hasread = models.CharField(max_length=3)
#    class Meta:
#        db_table = u'userpublicationmark'
#
#class Userrights(models.Model):
#    user_id = models.IntegerField(primary_key=True)
#    right_name = models.CharField(max_length=60, primary_key=True)
#    class Meta:
#        db_table = u'userrights'
#
#class Users(models.Model):
#    user_id = models.IntegerField(primary_key=True)
#    theme = models.CharField(max_length=765)
#    password_invalidated = models.CharField(max_length=15)
#    newwindowforatt = models.CharField(max_length=15)
#    summarystyle = models.CharField(max_length=765)
#    authordisplaystyle = models.CharField(max_length=765)
#    liststyle = models.IntegerField()
#    login = models.CharField(max_length=60)
#    password = models.CharField(max_length=765)
#    initials = models.CharField(max_length=30, blank=True)
#    firstname = models.CharField(max_length=765, blank=True)
#    betweenname = models.CharField(max_length=30, blank=True)
#    surname = models.CharField(max_length=765, blank=True)
#    csname = models.CharField(max_length=30, blank=True)
#    abbreviation = models.CharField(max_length=30)
#    email = models.CharField(max_length=765, blank=True)
#    u_rights = models.IntegerField()
#    lastreviewedtopic = models.IntegerField()
#    type = models.CharField(max_length=24)
#    lastupdatecheck = models.IntegerField()
#    exportinbrowser = models.CharField(max_length=15)
#    utf8bibtex = models.CharField(max_length=15)
#    language = models.CharField(max_length=60)
#    similar_author_test = models.CharField(max_length=60)
#    class Meta:
#        db_table = u'users'
#
#class Usertopiclink(models.Model):
#    user_id = models.IntegerField(primary_key=True)
#    topic_id = models.IntegerField()
#    star = models.IntegerField()
#    collapsed = models.IntegerField()
#    class Meta:
#        db_table = u'usertopiclink'
#


# vim:set ts=4 sw=4 et:
