// "The World Today" — make.fun news-image-20261127 entry, Node 22, standard
// library only. The front page is the entry.png stored beside this file, so
// the program just copies that file into the output directory the grader
// provides. The image was drawn in code (see render.py in this repository);
// nothing is fetched while it runs, which is why two runs write the same
// bytes. Locally, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const here = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(here, join(outDir, 'entry.png'));
