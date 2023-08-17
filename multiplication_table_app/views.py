from django.http import HttpResponse

def multiplication_table_view(request):
    # Your logic to generate the multiplication table goes here
    table_html = "<h1>Multiplication Table</h1>"
    # Generate the HTML for the multiplication table and store it in the table_html variable
    
    return HttpResponse(table_html)
