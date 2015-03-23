from django.shortcuts import render
from django.template import loader, Context
from django.http import Http404

def home(request):
    return render(request, 'home.html')

def project(request, project=None):
    param = {}
    pictures = []
    if project == 'feedr':
        param['project_name'] = 'FeedR'
        param['project_package'] = 'com.sokss.feedr.app'
        param['project_icon'] = 'feedr_icon.png'
        param['project_description'] = loader.get_template('feedr.html').render(Context())

        pictures = ['feedr/presentation_phone_1.png',
                    'feedr/presentation_phone_2.png',
                    'feedr/presentation_phone_3.png',
                    'feedr/presentation_phone_4.png',
                    'feedr/presentation_phone_5.png',
                    'feedr/presentation_1.png',
                    'feedr/presentation_2.png',
                    'feedr/presentation_3.png',
                    ]


    elif project == 'wizzluck':
        param['project_name'] = 'WizzLuck'
        param['project_package'] = 'com.appsclub.social.wizzluck'
        param['project_icon'] = 'wizzluck_icon.png'
        param['project_description'] = loader.get_template('wizzluck.html').render(Context())

        pictures = ['wizzluck/presentation_1.png',
                    'wizzluck/presentation_2.png',
                    'wizzluck/presentation_3.png',
                    'wizzluck/presentation_4.png'
                    ]
    elif project == 'memorizeit':
        param['project_name'] = 'MemorizeIt'
        param['project_package'] = 'com.sokss.memorize.app'
        param['project_icon'] = 'memorizeit_icon.png'
        param['project_description'] = loader.get_template('memorizeit.html').render(Context())

        pictures = ['memorizeit/presentation_1.png',
                    'memorizeit/presentation_2.png',
                    'memorizeit/presentation_3.png',
                    'memorizeit/presentation_4.png',
                    'memorizeit/presentation_5.png',
                    ]
    else:
        raise Http404

    param['pictures'] = pictures
    return render(request, 'project.html', param)

