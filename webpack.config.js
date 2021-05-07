const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
   entry: "./src/index.ts",
   output: {
      filename: "js/[name].js",
      path: path.resolve(__dirname, "static"),
   },

   devtool: "inline-source-map",

   stats: {
      children: true,
   },

   module: {
      rules: [
         {
            test: /\.ts$/,
            use: "ts-loader",
            exclude: /node_modules/,
         },

         {
            test: /\.(sa|sc|c)ss$/,
            use: [
               { loader: MiniCssExtractPlugin.loader },
               { loader: "css-loader" },
               {
                  loader: "sass-loader",
                  options: {
                     sourceMap: true,
                  },
               },
            ],
         },
      ],
   },

   plugins: [
      new MiniCssExtractPlugin({
         filename: "css/styles.css",
      }),
   ],

   resolve: {
      extensions: [".ts", ".js"],
   },
};
