# This script will create some users, supervisors, and projects!
# Note, if you run this more than once, you'll be creating user with the same
# name and duplicate supervisors. The script will still work, but you'll see some
# warnings.
from models import db,User,Supervisor,Project

# Create 2 users
abc = User("ABC")
xyz = User("XYZ")

# Add users to database
db.session.add_all([abc,xyz])
db.session.commit()

# Check with a query, this prints out all the users!
print(User.query.all())

# Grab ABC from database
# Grab all Users with the name "ABC", returns a list, so index [0]
# Alternative is to use .first() instead of .all()[0]
abc = User.query.filter_by(name='ABC').all()[0]

# Create an Supervisor to abc
sup_1 = Supervisor("SUPERVISOR 1",abc.id)

# Give some projects to abc
pro_1 = Project('Project 1',abc.id)
pro_2 = Project("Project 2",abc.id)

# Commit these changes to the database
db.session.add_all([sup_1, pro_1, pro_2])
db.session.commit()

# Let's now grab abc again after these additions
abc = User.query.filter_by(name='ABC').first()
print(abc)

# Show projects
abc.report_projects()

# You can also delete things from the database:
# find_user = User.query.get(1)
# db.session.delete(find_user)
# db.session.commit()
