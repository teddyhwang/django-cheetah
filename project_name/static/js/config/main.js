require.config({

    baseUrl: 'static/js/',

    waitSeconds: 30,

    shim: {

        // jQuery plugins (non-amd compliant) need this shim config
        // 'jquery-ui': {
        //  deps: ['jquery']
        // }

    },

    paths: {
        // jQuery
        'jquery'                    : '../lib/jquery/jquery.min',

        // Third Party Plugins

        // Setting Files
        'settings'                  : 'modules/settings',

        // Global Mediator
        'global'                    : 'mediators/global'
    }

});
