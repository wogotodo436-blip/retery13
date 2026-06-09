with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. tophud
content = content.replace(
    '              <LayoutGrid className="w-4 h-4" />\n            </button>\n          </motion.div>',
    '              <LayoutGrid className="w-4 h-4" />\n            </button>\n            </div>\n          </motion.div>',
)

# 2. decryptor
content = content.replace(
    "            )}\\n          </motion.div>\\n        )}".replace("\\n", "\n"),
    "            )}\\n            </div>\\n          </motion.div>\\n        )}".replace(
        "\\n", "\n"
    ),
)

# 3. parametris_efir
content = content.replace(
    "              </button>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n\n      <AnimatePresence>\n        {isMapSettingsOpen",
    "              </button>\n            </div>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n\n      <AnimatePresence>\n        {isMapSettingsOpen",
)

# 4. map 1
content = content.replace(
    "              </button>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n      <AnimatePresence>\n        {isSizeSettingsOpen",
    "              </button>\n            </div>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n      <AnimatePresence>\n        {isSizeSettingsOpen",
)

# 5. size
content = content.replace(
    '              <span className="text-slate-500 text-xs font-mono">Настройки размера (в разработке)</span>\n            </div>\n          </motion.div>',
    '              <span className="text-slate-500 text-xs font-mono">Настройки размера (в разработке)</span>\n            </div>\n            </div>\n          </motion.div>',
)

# 6. spheresize
content = content.replace(
    "                Сбросить параметры\n              </button>\n          </motion.div>",
    "                Сбросить параметры\n              </button>\n            </div>\n          </motion.div>",
)

# 7. perf
content = content.replace(
    "              </button>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n\n      <AnimatePresence>\n        {isMapSettingsOpen",
    "              </button>\n            </div>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n\n      <AnimatePresence>\n        {isMapSettingsOpen",
)

# 8. map 2
content = content.replace(
    "                )}\n              </div>\n            </motion.div>\n          )}",
    "                )}\n              </div>\n            </div>\n            </motion.div>\n          )}",
)

# 9. navigator
content = content.replace(
    "              </span>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n    </div>\n\n    <div",
    "              </span>\n            </div>\n            </div>\n          </motion.div>\n        )}\n      </AnimatePresence>\n    </div>\n\n    <div",
)

# 10. catalog
content = content.replace(
    "                  </>\n                )}\\n              </motion.div>\\n            </>\\n          )}".replace(
        "\\n", "\n"
    ),
    "                  </>\n                )}\n              </div>\n              </motion.div>\n            </>\n          )}",
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Applied div fixes")
