# views will handle logic for each URL

# Todo: create profile
#   view function or class?
#   will take and render a form:
#   if form is valid:
#       request POST
#       instantiate new model profile object
#    handle logic for skills:
#       display default list of skills
#       user choosing skills
#       user adding custom skills
#   render template:
#       form
#       return userprofile object

# Todo: edit profile
#   view function or class?
#   will take and render a form:
#       same form as create profile
#   if form is valid:
#       request PUT
#       updates appropriate model profile object
#    handle logic for skills:
#       display Users chosen/added skills
#       user deleting skills
#       user adding new skills
#       user updating skills
#   render template:
#       form
#       return userprofile object


# Todo: Display Profile
#   view function or class?
#       method: GET
#       interface with database through model objects
#       read data from data base table (query)
#       render data from database table to template
#   search function:
#       search form
#       send search as database query
#       display results of query
#   render template:
#       database query
#       return query
