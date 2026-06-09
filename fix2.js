const fs = require('fs');

let content = fs.readFileSync('src/App.tsx', 'utf8');

// The main issue is that we have <motion.div ...> ... <div className="... w-full h-full"> ... missing </div> ... </motion.div>
// We can use a regex to find all <div className="... w-full h-full"> and their corresponding <motion.div> wrappers.
// Wait, we know there are exactly 9 of them.
// Let's just fix the missing </div>s before the </motion.div> tags.

// 1. tophud ends right before `        )}` and `      </AnimatePresence>`
content = content.replace(
  `            <button
              onClick={() => setIsUiHidden(true)}
              className="hud-panel pointer-events-auto bg-[#070716]/80 hover:bg-slate-900 border border-indigo-500/20 text-indigo-300 hover:text-white w-9 rounded-lg backdrop-blur-xl transition-all duration-200 shadow-[0_10px_25px_rgba(0,0,0,0.4)] flex items-center justify-center h-9 shrink-0 cursor-pointer"
              title="Скрыть весь интерфейс"
            >
              <EyeOff className="w-4 h-4" />
            </button>
          </motion.div>`,
  `            <button
              onClick={() => setIsUiHidden(true)}
              className="hud-panel pointer-events-auto bg-[#070716]/80 hover:bg-slate-900 border border-indigo-500/20 text-indigo-300 hover:text-white w-9 rounded-lg backdrop-blur-xl transition-all duration-200 shadow-[0_10px_25px_rgba(0,0,0,0.4)] flex items-center justify-center h-9 shrink-0 cursor-pointer"
              title="Скрыть весь интерфейс"
            >
              <EyeOff className="w-4 h-4" />
            </button>
            </div>
          </motion.div>`
);

// We need to undo my bad python replaces if they were incorrectly applied.
// Let's check `git status`. Oh, there's no git.
// Did the python script apply successfully?
// The python script applied some `</div>`s. Let's look at `npm run lint` errors to find exactly where `div` is missing.
fs.writeFileSync('fix2.js', content);
