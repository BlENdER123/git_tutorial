// подключение всех необходимых библиотек
var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');

// основная функция
function copy(done) {

    // указываем путь к файлу scss
    gulp.src('./styles/main.scss')
    // запускаем компиляцию для scss с отслеживание ошибок
    .pipe(sass({
        errLogToConsole: true
    }))
    .on('error', console.error.bind(console))
    // добавляем авто префиксы
    .pipe(autoprefixer({
        cascade: false
    }))
    // переименновываем файл
    .pipe(rename('main.css'))
    // сохраняем в нужную папку
    .pipe( gulp.dest('./css/') );

    done();
}

// задаем стандартное задание
gulp.task('default', copy)