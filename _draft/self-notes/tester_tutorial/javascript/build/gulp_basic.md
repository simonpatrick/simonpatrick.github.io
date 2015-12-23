# gulp intro
gulp is a build tool for javascript application

## gulpfile

guplfile.js file:

```javascript
var gulp =require('gulp')
gulp.src('lib/**/*.js')
    .pipe(concat())
    .pipe(rename('concat.js'))
    .pipe(gupl.dest('build'))
```

run:
```shell
gulp
```
