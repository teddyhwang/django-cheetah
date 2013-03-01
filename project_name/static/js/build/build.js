
// An example of a build.js using r.js
// http://requirejs.org/docs/optimization.html
// https://github.com/jrburke/r.js/blob/master/build/example.build.js
// run `node r.js -o build.js` from terminal

({
    appDir: '../',
    baseUrl: '../',
    dir: '../../../www/static/js/',
    optimize: 'uglify',
    optimizeCss: 'none', // https://github.com/jrburke/r.js/issues/167

    mainConfigFile: '../config/main.js',
    fileExclusionRegExp: /^(node_modules|.svn)/,

    // Uncomment to include "on demand" require dependencies
    // findNestedDependencies: true,

    modules: [
        {
            name: 'global'
        }
    ]
})
