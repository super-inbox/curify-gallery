const fs=require('fs'),path=require('path'),sharp=require('/Users/qqwjq/curify-frontend/node_modules/sharp');
const {applyTiledWatermark}=require('/Users/qqwjq/curify-frontend/scripts/lib/watermark.cjs');
(async()=>{let count=0;for(const c of JSON.parse(fs.readFileSync(path.join(__dirname,'batch.json')))){
 const srcCheck=path.join(__dirname,'cards',c.id+'.png');
 if(!fs.existsSync(srcCheck) || !fs.existsSync(path.join(__dirname,'video',c.id+'.mp4'))) {if(process.argv.includes('--partial'))continue; throw Error('Missing finished card/video '+c.id);}
 const stem='template-hsk-bilingual-reading-text-lesson-poster-'+c.id;
 const src=path.join(__dirname,'cards',c.id+'.png');
 const out=path.join(__dirname,'publish/images',stem+'.jpg');
 applyTiledWatermark(src,out);
 await sharp(out).resize({width:512,height:512,fit:'inside'}).jpeg({quality:88}).toFile(path.join(__dirname,'publish/previews',stem+'-prev.jpg'));
 fs.copyFileSync(path.join(__dirname,'video',c.id+'.mp4'),path.join(__dirname,'publish/video',stem+'.mp4')); count++;
}console.log('Prepared '+count+' watercolor posters, previews and videos.');})().catch(e=>{console.error(e);process.exit(1)});
