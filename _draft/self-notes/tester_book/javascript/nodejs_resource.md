# Awesome Node.js

A curated list of astonishing Node.js frameworks, libraries and resources. Inspired by [awesome-php](https://github.com/ziadoz/awesome-php) and [awesome-python](https://github.com/vinta/awesome-python).

Your pull requests are very welcome! Let's make this the awesomest resource for Node!

- [Awesome Node.js](#awesome-nodejs)
    - [Application Servers](#application-servers)
    - [Async Control Flow](#async-control-flow)
    - [Authentication and OAuth](#authentication-and-oauth)
    - [Build Tools](#build-tools)
    - [Communication](#communication)
    - [Content Management System](#content-management-system)
    - [Database Drivers](#database-drivers)
    - [Debugging Tools](#debugging-tools)
    - [Documentation](#documentation)
    - [Environment Management](#environment-management)
    - [Files and MIME Type Manipulation](#files-and-mime-type-manipulation)
    - [Forms](#forms)
    - [Integrated Development Environments](#integrated-development-environments)
    - [Logging](#logging)
    - [ORM](#orm)
    - [Package Management](#package-management)
    - [Rate Limiting](#rate-limiting)
    - [RESTful API](#restful-api)
    - [Science](#science)
    - [Templating](#template-engine)
    - [Testing](#testing)
    - [Tools for building CLIs](#tools-for-building-clis)
    - [Web Frameworks](#web-frameworks)
    - [Miscellaneous](#miscellaneous)
- [Tutorials](#tutorials)
- [Books](#books)
- [Blogs](#blogs)
- [Other Awesome Lists](#other-awesome-lists)

## Application Servers

*Application Server is an environment to run and manage multiple applications.*

* [Impress](https://github.com/tshemsedinov/impress) - Impressive multipurpose scalable Application Server optimized for high load API and web applications.

## Async Control Flow

*Libraries that help you manage asyncronous control flow and avoid callback hell.*

* Callback-based:
    * [Async](https://github.com/caolan/async) - Utility module which provides straight-forward, powerful functions for working with asynchronous JavaScript.
    * [each-async](https://github.com/sindresorhus/each-async) - Async concurrent iterator like forEach.
    * [node-seq](https://github.com/substack/node-seq) - Chainable asynchronous flow control for node.js with sequential and parallel primitives and pipeline-style error handling.
* Promise-based ([Promises/A+](http://promises-aplus.github.io/promises-spec/)):
    * [Bluebird](https://github.com/petkaantonov/bluebird) - Bluebird is a fully featured promise library with focus on innovative features and performance.
    * [Q](https://github.com/kriskowal/q) - Full-featured promise library with large API covering any situation you may encounter.
    * [RSVP.js](https://github.com/tildeio/rsvp.js) - Lightweight, but still compliant, promise library.
    * [when.js](https://github.com/cujojs/when) - Rock solid, battle tested promise library.
* Fibers-base ([node-fibers](https://github.com/laverdet/node-fibers/)):
    * [asyncawait](https://github.com/yortus/asyncawait) - Inspired by C# async/await feature, implementation of the same patter using fibers.
* Generator-based:
    * [Co](https://github.com/visionmedia/co) - Generator based flow-control goodness for nodejs and the browser.
    * [suspend](https://github.com/jmar777/suspend) - Generator-based control flow that plays nice with callbacks, promises, and thunks.

## Authentication and OAuth

*Libraries for implementing authentications schemes.*

* [everyauth](https://github.com/bnoguchi/everyauth) - Authentication and authorization (password, facebook, & more) for your Connect and Express apps.
* [ldapjs](http://ldapjs.org/) - Pure JavaScript, from-scratch framework for implementing LDAP clients and servers.
* [Lockit](https://github.com/zemirco/lockit) - Full featured authentication solution for Express.
* [oauth-signature-js](https://github.com/bettiolo/oauth-signature-js) - OAuth 1.0a signature generator
* [PassportJS](http://passportjs.org/) - Simple authentication middleware framework.
* [passwordless](https://passwordless.net) - Token-based authentication middleware for Express allowing authentication without passwords.

## Build Tools

*Libraries for building and task running*

* [Browserify](http://browserify.org/) - Browserify lets you require('modules') in the browser by bundling up all of your dependencies.
* [Grunt.js](http://gruntjs.com/) - A task runner to ease epetitive tasks like unit testing, compilation and so on.
* [Gulp.js](http://gulpjs.com/) - A streaming build system which use of streams and code-over-configuration.
* [Nodemon](http://nodemon.io/) - A dev utility that monitor any changes in source and automatically restart server.

## Communication

* [BinaryJS](http://binaryjs.com/) - BinaryJS is bidrectional realtime binary data with binary websockets
* [Primus](https://github.com/primus/primus) - An abstraction layer for real-time frameworks to prevent module lock-in.
* [Socket.IO](http://socket.io/) - Websocket framework for Node and Javascript.
* [SocketCluster](https://github.com/topcloud/socketcluster) - Scalable HTTP + WebSocket engine which can run on multiple CPU cores.
* [SockJS](https://github.com/sockjs) - Websocket emulation.
* [Straw](https://github.com/simonswain/straw) - Real-time dataflow framework.

## Content Management System

* [Calipso](http://calip.so/) - Calipso is a simple CMS, built along similar themes to Drupal and Wordpress.
* [KeystoneJS](http://keystonejs.com/) - Node.js CMS and web application platform built on Express and MongoDB.

## Database Drivers

*Libraries for connecting and operating databases*

* [Node-mongodb-native](https://github.com/mongodb/node-mongodb-native/) - Mongo DB Native NodeJS Driver.
* [Node-mysql](https://github.com/felixge/node-mysql/) - A pure node.js JavaScript Client implementing the MySql protocol.
* [Node-redis](https://github.com/mranney/node_redis) - Redis Driver, use [hideredis](https://github.com/redis/hiredis-node) for native parser, and checkout [then-redis](https://github.com/mjackson/then-redis) for a Promise-based API.

## Debugging Tools

*Tools for debugging Node applications*

* [cf-node-debug](https://www.npmjs.org/package/cf-node-debug) - Proxy to aid in debugging node running on a PaaS.
* [debug](https://github.com/visionmedia/debug) - Tiny debugging utility.
* [jstrace](https://github.com/jstrace/jstrace) - Dynamic tracing for JavaScript, similar to dtrace, ktap etc.
* [longjohn](https://github.com/mattinsler/longjohn) - Longer stack traces for Node.
* [node-inspector](https://github.com/node-inspector/node-inspector) - Node.js debugger based on Blink Developer Tools.
* [Nodev](https://github.com/akamensky/nodev) - Tool for easier debugging based on nodemon and node-inspector.
* [stackman](https://github.com/watson/stackman) - Enhance an error stacktrace with code excerpts and other goodies.
* [Theseus](https://github.com/adobe-research/theseus) - A new type of JavaScript debugger featuring real-time code coverage, retroactive inspection and asynchronous call tree.
* [TraceGL](https://github.com/traceglMPL/tracegl) - Transforms your JavaScript, injecting monitoring code that produces a log of everything that happens.
* [TypesJs](https://github.com/ChrisAntaki/typesjs) - Easy type checking, for Node & browsers.
* [vstream](https://github.com/joyent/node-vstream) - Instrumentable streams mix-ins to inspect a pipeline of streams.

## Documentation

*Libraries for generating project documentation.*

* [Docco](http://jashkenas.github.io/docco/) - Docco is a quick-and-dirty documentation generator, written in Literate CoffeeScript.
* [dox](https://github.com/visionmedia/dox) - JavaScript documentation generator for node using markdown and jsdoc.
* [Groc](https://github.com/nevir/groc) - Documentation generation, in the spirit of literate programming.

## Environment Management

*Libraries for Node version and environment management.*

* [n](https://github.com/visionmedia/n) - Node version management.
* [nave](https://github.com/isaacs/nave) - Virtual Environments for Node.
* [nodeenv](https://github.com/ekalinin/nodeenv) - Virtual environment for Node.js & integrator with virtualenv.
* [nvm](https://github.com/creationix/nvm) - Node Version Manager (does not require prior installation of node).

## Files and MIME Type Manipulation

* [PDFKit](http://pdfkit.org/) - A JavaScript PDF generation library for Node and browser.

## Forms

*Libraries for deal with forms and form data*

* [express-validator](https://github.com/ctavan/express-validator) - An express.js middleware for node-validator.
* [node-validator](https://github.com/chriso/validator.js) - A simple string validation and sanitization.

## Integrated Development Environments

*IDEs and Editors for development*

* [Atom](https://github.com/atom/atom) - The hackable editor by GitHub
* [Brackets](https://github.com/adobe/brackets) - An open source code editor for the web, written in JavaScript, HTML and CSS.
* [Cloud Commander](http://cloudcmd.io) - Web file manager. Has editor and console. Allows you to develop web applications, sites etc.
* [Cloud9](https://c9.io/site/code-smarter-code-together/) - Web editor with collaboration tools.
* [CmdEr](https://github.com/bliker/cmder) - Not really and IDE, but a great "lovely console emulator package for Windows"
* [Enide](http://www.nodeclipse.org/enide/) - Node Eclipse IDE with Nodeclipse plugin.
* [InteliJIDEA](http://www.jetbrains.com/idea/features/nodejs.html) - Fast Node plugin for InteliJ.
* [Notepad++](http://notepad-plus-plus.org) - Notepad++ is a free source code editor and Notepad replacement that supports several languages.
* [Visual Studio](http://www.visualstudio.com/) - With [Node.js Tools for Visual Studio](https://nodejstools.codeplex.com/) (Supports editing, IntelliSense, profiling, npm, TypeScript, debugging locally and remotely on Windows/MacOS/Linux)
* [Webstorm](http://www.jetbrains.com/webstorm/features/#node.js) - "Create great websites and applications in a great IDE. The best JavaScript IDE and HTML editor is at your service."

## Logging

*Tools for generating and working with log files.*

* [Bunyan](https://github.com/trentm/node-bunyan) - A simple and fast JSON logging module for node.js services.
* [caterpillar](https://github.com/bevry/caterpillar) - A logging system that can log and pipe the output off to different locations.
* [intel](https://seanmonstar.github.io/intel) - A comprehensive logging library (handlers, filters, formatters, console injection).
* [Log.io](http://logio.org/) - Real time logging facility on the browser.
* [tracer](https://github.com/baryon/tracer) - A powerful and customizable logging library for node.js.
* [winston](https://github.com/flatiron/winston) - A multi-transport async logging library.

## ORM

*Libraries that implement Object-Relational Mapping or datamapping techniques.*

* [Mongoose](http://mongoosejs.com/) - Almost an ORM for mongodb.
* [Node-orm2](https://github.com/dresende/node-orm2) - Another Relational Object Mapper.
* [Sequelize](http://sequelizejs.com/) - Sequelize library provides easy access to MySQL, MariaDB, SQLite or PostgreSQL databases.
* [Waterline](https://github.com/balderdashy/waterline) - Datastore-agnostic tool that dramatically simplifies interaction with one or more databases.

## Package Management

*Libraries for package and dependency management.*

* [Duo](http://duojs.org/) - A next-generation package manager for the front-end.
* [npm](https://www.npmjs.org/) - Default package manager. Installs, publishes and manages node programs.

## Rate Limiting

*Libraries that help restrict the frequency of certain actions.*

* [Bottleneck](https://github.com/SGrondin/bottleneck) - A powerful rate limiter that makes throttling easy.

## RESTful API

*Libraries for developing RESTful APIs.*

* [Heimdall](https://github.com/binarymax/heimdall) - REST API Guardian for Express.
* [Node-restify](http://mcavage.me/node-restify/) - A node.js module built specifically to build correct REST web services.
* [Sails](http://sailsjs.org) - MVC framework which generates a RESTful JSON API.

# Science

*Things some awesome crazy people are doing!*

* [BitcoinJS](http://bitcoinjs.org) - Clean, readable, proven Bitcoin library.
* [Breach](http://breach.cc) - Modular and hackable browser written in JavaScript.
* [dat](http://dat-data.com) - Real-time replication and versioning for data sets.
* [ipfs](https://github.com/jbenet/node-ipfs) - Distributed file system that seeks to connect all computing devices with the same system of files.
* [js-git](https://github.com/creationix/js-git) - JavaScript implementation of Git.
* [NodeOS](http://node-os.com) - The first operating system powered by npm.
* [PDFKit](http://pdfkit.org) - PDF generation library.
* [peercast](https://github.com/mafintosh/peercast) - Stream a torrent video to Chromecast.
* [peerflix](https://github.com/mafintosh/peerflix) - Streaming torrent client.
* [peerwiki](https://github.com/mafintosh/peerwiki) - All of Wikipedia on BitTorrent.
* [turf](https://github.com/Turfjs/turf/) - Modular geospatial processing and analysis engine.
* [webtorrent](https://github.com/feross/webtorrent) - Streaming torrent client for Node.js and the browser.

## Templating

*Libraries and tools for templating and lexing.*

* [ECT](http://ectjs.com/) - "Fastest JavaScript template engine with embedded CoffeeScript syntax" as they say (benchmark proof).
* [handlebars.js](https://github.com/wycats/handlebars.js/) - A superset of Mustache templates which adds powerful features like helpers and more advanced blocks.
* [hogan.js](http://twitter.github.io/hogan.js/) - Twitter's small, fast, phase-separated compiler for Mustache templates.
* [Jade](http://jade-lang.com/) - Handful node template engine.
* [nunjucks](https://github.com/mozilla/nunjucks) - A powerful templating engine with inheritance, asynchronous control, and more (jinja2 inspired).
* [Swig](http://paularmstrong.github.io/swig/) - A simple, powerful, and extendable JavaScript Template Engine.

## Testing

*Testing frameworks.*

* [chai](https://github.com/chaijs/chai) - BDD / TDD assertion framework for node.js and the browser that can be paired with any testing framework.
* [Concrete](http://ryankee.github.io/concrete/) - Continuous integration server.
* [Expresso](http://visionmedia.github.io/expresso/) - TDD framework for Node.
* [Jasmine](http://jasmine.github.io/) - Simple Behavioral tests for Node and Javascript.
* [Jezebel](https://github.com/benrady/jezebel) - A REPL and continuous test runner for Node.js Jasmine tests.
* [mocha](https://github.com/visionmedia/mocha) - Mocha is a feature-rich JavaScript test framework running on node.js and the browser, making asynchronous testing simple and fun.
* [Mochify](https://github.com/mantoni/mochify.js) - TDD with Browserify, Mocha, PhantomJS and WebDriver.
* [NodeUnit](https://github.com/caolan/nodeunit) - Simple syntax unit test tool.
* [ready.js](http://dsimard.github.io/ready.js/) - Continuous javascript integration tool.
* [should.js](https://github.com/visionmedia/should.js) - BDD style assertions for node.js -- test framework agnostic.
* [sinon](http://sinonjs.org/) - Standalone test spies, stubs and mocks for JavaScript.
* [tape](https://github.com/substack/tape) - tap-producing test harness for node and browsers.

## Tools for building CLIs

*Libraries and tools which support you by building Command-Line Interfaces.*

* [blessed](https://github.com/chjj/blessed) - A curses-like library for node.js.
* [chalk](https://github.com/sindresorhus/chalk) - Terminal string styling done right
* [cli-spinner](https://github.com/helloIAmPau/node-spinner) - A simple spinner for node cli.
* [cli-table](https://github.com/LearnBoost/cli-table) - Pretty unicode tables for the CLI with Node.JS
* [cli](https://github.com/chriso/cli) - Rapidly build command line apps with node.
* [colors.js](https://github.com/Marak/colors.js) - get colors in your node.js console like what.
* [commander.js](https://github.com/visionmedia/commander.js) - The complete solution for node.js command-line interfaces, inspired by Ruby's commander.
* [configstore](https://github.com/yeoman/configstore) - Easily load and persist config without having to think about where and how.
* [Inquirer](https://github.com/SBoudrias/Inquirer.js) - A collection of common interactive command line user interfaces. *Ask questions, parsing, validating answers, managing hierarchical prompts and providing error feedback.*
* [log-symbols](https://github.com/sindresorhus/log-symbols) - Colored symbols for various log levels.https://github.com/sindresorhus/log-symbols
* [minimist](https://github.com/substack/minimist) - Simple module for command line arguments parsing.
* [nomnom](https://github.com/harthur/nomnom) - Option parser for node with generated usage and commands.
* [read](https://github.com/isaacs/read) - For reading user input from stdin.
* [terminal-menu](https://github.com/substack/terminal-menu) - retro ansi terminal menus for serious 80s technicolor business.
* [text-table](https://github.com/substack/text-table) - generate borderless text table strings suitable for printing to stdout.

## Web Frameworks

*Web development frameworks.*

* [Derby](https://github.com/derbyjs/derby) - MVC framework making it easy to write realtime, collaborative applications that run in both Node.js and browsers.
    * [Derby-awesome](https://github.com/onerussell/awesome-derby) - A collection of awesome derby components
* [Express](http://expressjs.com/) -  A minimal and flexible node.js web application framework.
* [Flatiron](http://flatironjs.org/) - An adaptable framework for building modern web applications.
* [Hapi](https://github.com/spumko/hapi) - A rich framework for building applications and services.
* [HuntJS](https://huntjs.herokuapp.com/) - event driven framework for building clustered webservers, telnet and background applications with mongoose or sequilize as data storage.
* [Interfake](https://github.com/basicallydan/interfake) - Rapid prototyping framework for making mock HTTP APIs, with a Node, command-line and HTTP interface.
* [Koa](http://koajs.com/) - A framework which aims to be a smaller, more expressive, and more robust foundation for web applications.
* [LoopBack](http://loopback.io/) - Powerful Node.js framework for creating APIs and easily connecting to backend data sources.
* [Meteor](https://www.meteor.com/) - A platform that has strong features such as live page update, sync and hopt code pushes.
* [Restify](http://mcavage.me/node-restify/) - A node framework built specifically to enable you to build correct REST web services.
* [SailsJS](http://sailsjs.org) - An MVC web framework with a modern twist, supporting WebSockets, streams, and a data-driven API.
* [Totaljs](http://www.totaljs.com/) - Friendly responsive design web application framework for node.

## Content Management System

* [Calipso](http://calip.so/) - Calipso is a simple CMS, built along similar themes to Drupal and Wordpress.
* [KeystoneJS](http://keystonejs.com/) - Node.js CMS and web application platform built on Express and MongoDB.


## Miscellaneous

*Miscellaneous Tools which doesn't fit to the other categories.*

* [agenda](https://github.com/rschmukler/agenda) - Lightweight job scheduling on MongoDB.
* [atom-shell](https://github.com/atom/atom-shell) - Cross-platform desktop application shell.
* [Bottleneck](https://github.com/SGrondin/bottleneck) - A powerful rate limiter that makes throttling easy.
* [cheerio](https://github.com/cheeriojs/cheerio) - Fast, flexible, and lean implementation of core jQuery designed specifically for the server.
* [common-errors](https://github.com/shutterstock/node-common-errors) - Common error classes and utility functions.
* [Faker.js](https://github.com/Marak/Faker.js) - Generate massive amounts of fake data.
* [Github Linker](https://chrome.google.com/webstore/detail/github-linker/jlmafbaeoofdegohdhinkhilhclaklkp) - Chrome extension that linkifies dependencies in package.json on GitHub.
* [lazy-req](https://github.com/sindresorhus/lazy-req) - Require modules lazily.
* [multiline](https://github.com/sindresorhus/multiline) - Multiline strings in JavaScript.
* [nan](https://github.com/rvagg/nan) - A header file filled with macro and utility goodness for making add-on development for across Node.js versions easier.
* [Node-Bell](https://github.com/eleme/node-bell) - Real-time anomalies detection for periodic time series.
* [node-pre-gyp](https://github.com/mapbox/node-pre-gyp/) - Makes it easy to publish and install Node.js C++ addons from binaries.
* [opencv](https://github.com/peterbraden/node-opencv) - Bindings for OpenCV. The defacto computer vision library.
* [opn](https://github.com/sindresorhus/opn) - Opens stuff like websites, files, executables.
* [require-uncached](https://github.com/sindresorhus/require-uncached) - Require a module bypassing the cache.
* [semver](https://github.com/isaacs/node-semver) - [semver](http://semver.org) parser.
* [shelljs](https://github.com/arturadib/shelljs) - Portable Unix shell commands.
* [ssh2](https://github.com/mscdex/ssh2) - An SSH2 client module.
* [stringify-object](https://github.com/yeoman/stringify-object) - Stringify an object/array like JSON.stringify just without all the double-quotes.
* [strip-bom](https://github.com/sindresorhus/strip-bom) - Strip UTF-8 byte order mark (BOM) from a string/buffer/stream.
* [webworker-threads](https://github.com/audreyt/node-webworker-threads) - Lightweight Web Worker API implementation with native threads.

# Tutorials

* [browserify-handbook](https://github.com/substack/browserify-handbook) - The definitive guide for browserify.
* [module-best-practices](https://github.com/mattdesl/module-best-practices) - Some good practices when writing new npm modules.
* [Nodeschool](http://nodeschool.io) - Learn Node.js with interactive lessons.
* [stream-handbook](https://github.com/substack/stream-handbook) - How to write Node.js programs with streams.
* [The Art of Node](https://github.com/maxogden/art-of-node/#the-art-of-node) - An introduction to Node.js.

# Books

* [Mastering Node](http://tj.github.io/masteringnode/)
* [Mixu's Node book](http://book.mixu.net/node/)
* [Node.js in Action](http://www.amazon.com/Node-js-Action-Mike-Cantelon/dp/1617290572)
* [Practical Node.js: Building Real-World Scalable Web Apps](http://practicalnodebook.com)
* [Professional Node.js: Building Javascript Based Scalable Software](http://www.amazon.com/Professional-Node-js-Building-Javascript-Scalable-ebook/dp/B009L7QETY/)
* [Web Development with Node and Express](http://shop.oreilly.com/product/0636920032977.do)

# Blogs

* [HowToNode](http://howtonode.org) - Teaching how to do various tasks in Node.js as well as teach fundamental concepts that are needed to write effective code.
* [Node.js blog](http://blog.nodejs.org)

# Other Awesome Lists

Other amazingly awesome lists can be found in the [awesome-awesome](https://github.com/emijrp/awesome-awesome) and [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) projects.

# Contributing

[Chinese awesome-nodejs version](https://github.com/ueqt/awesome-nodejs) by @ueqt.

Your contributions are always welcome!
