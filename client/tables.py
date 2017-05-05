import django_tables2 as tables
from .models import Site

class LinkColumn(tables.Column):
    def render(self, value):
        return format_html('<a href=>{}</a>', value) 

class SiteTable(tables.Table):
    id = LinkColumn()
    name = LinkColumn()
    class Meta:
        model = Site
        
        
