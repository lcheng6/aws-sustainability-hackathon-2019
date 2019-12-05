/*NVDI has a numerical range of -1 to 1.  -1 is large body of water, closer to -1 could be cloud cover, some where between -.1 to .1
  is dirt and rocks.  And for the purpose of looking over results, I will use green color to mark everything above .3, because they look
  like a good discriminator for tree foliage.  The sample is just 2 colors: green for tree cover, and orange red ish for no tree
 */

let ndvi = (B08 - B04) / (B08 + B04);

return colorBlend(ndvi,
    [-0.2, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ],
    [[0, 0, 0],							   //  < -.2 = #000000 (black)
        [165/255,0,38/255],        //  -> 0 = #a50026
        [165/255,0,38/255],   //  -> .1 = #a50026
        [165/255,0,38/255],  //  -> .2 = #a50026
        [165/255,0,38/255],  //  -> .3 = #a50026
        [0,104/255,55/255], //  -> .4 = #006837
        [0,104/255,55/255], //  -> .5 = #006837
        [0,104/255,55/255], //  -> .6 = #006837
        [0,104/255,55/255], //  -> .7 = #006837
        [0,104/255,55/255],  //  -> .8 = #006837
        [0,104/255,55/255],   //  -> .9 = #006837
        [0,104/255,55/255]         //  -> 1.0 = #006837
    ]);
