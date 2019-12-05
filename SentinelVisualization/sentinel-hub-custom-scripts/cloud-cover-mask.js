/* this particular mask produce the greyscale mask based on cloud
   it's greyscale and not boolean mapping, because some clouds are completely
   opaque, and some is actually "see-through", it's up to you how you want to deal with it.
   converted from this source:
   https://github.com/sentinel-hub/custom-scripts/tree/master/sentinel-2/cby_cloud_detection
 */

function index(x, y) {
    return (x - y) / (x + y);
}
cd
function clip(a) {
    return Math.max(0, Math.min(1, a));
}


let bRatio = (B03 - 0.175) / (0.39 - 0.175);
let NDGR = index(B03, B04);
let gain = 2.5;

if (B11>0.1 && bRatio > 1) { //cloud
    var v = 0.5*(bRatio - 1);
    return [B04, B03, B02].map(a => gain * a);
    return [0.5*clip(B04), 0.5*clip(B03), 0.5*clip(B02) + v];
}

if (B11 > 0.1 && bRatio > 0 && NDGR>0) { //cloud
    var v = 5 * Math.sqrt(bRatio * NDGR);
    return [B04, B03, B02].map(a => gain * a);
    return [0.5 * clip(B04) + v, 0.5 * clip(B03), 0.5 * clip(B02)];
}
gain =0

return [B04, B03, B02].map(a => gain * a);