"use strict";
exports.__esModule = true;
var path = require("path");
var vscode_theme_generator_1 = require("vscode-theme-generator");
var themeName = 'Generated';
var colors = {
    black: '#222731',
    white: '#C0C5CE',
    blue: '#5196C6',
    red: '#C9538C',
    green: '#679C76',
    yellow: '#EBCB8B'
};
var colorSet = {
    base: {
        background: colors.black,
        foreground: colors.white,
        color1: colors.blue,
        color2: colors.red,
        color3: colors.green,
        color4: colors.yellow
    }
};
vscode_theme_generator_1.generateTheme(themeName, colorSet, path.join(__dirname, 'theme.json'));
