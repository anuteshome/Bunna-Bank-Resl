{
    'name': "Bunna Bank",
    'version': '17.0',
    'depends': ['base','mail'],
    'author': "Bunna Bank Team",
    'category': 'Services',
    'description': """
    Description text
    """,
  'sequence': -99999,
    # data files always loaded at installation
    'data': [
        # 'views/mymodule_view.xml',
        'security/ir.model.access.csv',
        'Views/Branch.xml',
        'Views/hr.xml',
        'Views/Employees.xml'  
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'data/demo_data.xml',
    ],
   'installable': True,
    'application': True,  # Set to False if it's not a standalone app
    'auto_install': False,
    #  'icon': '/Bunna_Bank/static/image/AnanyaT.jpg',
     'icon': '/Testing/static/image/image.png',

}