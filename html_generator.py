#html code generator program


#To generate code the user/programmer must define a list of titles and descriptions. As shown by the list defined below.
List_of_Titles_and_Descriptions = [ [title1, description1], [title2, description2], [title3, description3], [title4, description4]]


#This method writes html for one title and description
def generate_concept_HTML(concept_title, concept_description):
html_text_1 = '''
<div class="concept">
            <div class="concept-title">
                ''' + concept_title
            html_text_2 = '''
            </div>
            <div class="concept-description">
                ''' + concept_description
            html_text_3 = '''
            </div>
</div>'''
            full_html_text = html_text_1 + html_text_2 + html_text_3
            return full_html_text


# This method takes a list with two elements and uses the previous method to write code
def make_HTML(concept):
    title = concept[0]
    description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)




# This method takes an single list composed of nested lists of titles and descriptions and uses the previous two methods and a for loop to write code for all of them in a single step.


def make_HTML_for_many_concepts(list_of_concepts):
    code = ''
    for list in list_of_concepts:
        code += make_HTML(list)
    return code
        
#This last line tests my code.  
print make_HTML_for_many_concepts(List_of_Titles_and_Descriptions)
