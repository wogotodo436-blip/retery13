const fs = require('fs');

let content = fs.readFileSync('src/App.tsx', 'utf8');

// Undo bad `</div>` insertions from previous scripts
content = content.replace(/<\/div>\s*<\/motion\.div>/g, '</motion.div>');
content = content.replace(/<\/div>\s*<\/motion\.div>\s*<\/>\s*\}\)/g, '</motion.div>\n            </>\n          )}');

// Find every instance of `<div className={... w-full h-full"}>`
// We need to match its closing `</div>`.
// Since we wrapped the ENTIRE content of motion.div in this new div,
// the `</div>` should go exactly before the closing `</motion.div>` of that panel.

// Let's do a simple tag balancer for `<motion.div`
let newContent = '';
let i = 0;

while (i < content.length) {
    let motionDivStart = content.indexOf('<motion.div', i);
    if (motionDivStart === -1) {
        newContent += content.slice(i);
        break;
    }

    // Check if this motion.div has a `w-full h-full` div inside it
    let motionDivEndPos = content.indexOf('>', motionDivStart) + 1;
    let nextDivPos = content.indexOf('<div', motionDivEndPos);

    let isPanel = false;
    if (nextDivPos !== -1 && nextDivPos < motionDivEndPos + 200) {
        let nextDivEnd = content.indexOf('>', nextDivPos) + 1;
        let divTag = content.slice(nextDivPos, nextDivEnd);
        if (divTag.includes('w-full h-full')) {
            isPanel = true;
        }
    }

    // We need to find the matching </motion.div> for this <motion.div>
    let depth = 0;
    let curr = motionDivStart;
    let matchingEnd = -1;

    while (curr < content.length) {
        let nextOpen = content.indexOf('<motion.div', curr + 1);
        let nextClose = content.indexOf('</motion.div>', curr + 1);

        if (nextClose === -1) break;

        if (nextOpen !== -1 && nextOpen < nextClose) {
            depth++;
            curr = nextOpen;
        } else {
            if (depth === 0) {
                matchingEnd = nextClose;
                break;
            } else {
                depth--;
                curr = nextClose;
            }
        }
    }

    if (isPanel && matchingEnd !== -1) {
        // Insert </div> before </motion.div>
        newContent += content.slice(i, matchingEnd);
        newContent += '</div>\n            ';
        newContent += content.slice(matchingEnd, matchingEnd + 13); // </motion.div>
        i = matchingEnd + 13;
    } else {
        newContent += content.slice(i, motionDivEndPos);
        i = motionDivEndPos;
    }
}

fs.writeFileSync('src/App.tsx', newContent);
console.log('Fixed div closures');
