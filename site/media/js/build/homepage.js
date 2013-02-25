
// An example of a build.js using r.js
// http://requirejs.org/docs/optimization.html
// https://github.com/jrburke/r.js/blob/master/build/example.build.js
// run `node r.js -o build.js` from terminal

({
    baseUrl: '../',
    optimize: 'uglify',
    optimizeCss: 'none', // https://github.com/jrburke/r.js/issues/167
    mainConfigFile: '../config/homepage.js',
    name: '../../lib/almond/almond',
    include: ['config/homepage'],
    insertRequire: ['config/homepage'],
    out: '../../compiled/js/homepage.min.js',
    wrap: true
})
