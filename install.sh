#!/usr/bin/env bash
# Antigravity Skill Installer for Linux / macOS
# Skill: youth-tax-calculator

set -e

echo "Installing youth-tax-calculator skill to Antigravity global config..."

TARGET_DIR="$HOME/.gemini/config/skills/youth-tax-calculator"
mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SOURCE_DIR="$SCRIPT_DIR/skills/youth-tax-calculator"

if [ -d "$SOURCE_DIR" ]; then
    cp -rf "$SOURCE_DIR"/* "$TARGET_DIR/"
else
    FALLBACK_FILE="$SCRIPT_DIR/bd-income-tax-filing.SKILL.md"
    cp -f "$FALLBACK_FILE" "$TARGET_DIR/SKILL.md"
fi

# Clean up obsolete previous folders
rm -rf "$HOME/.gemini/config/skills/bd-youth-tax-expert" "$HOME/.gemini/config/skills/bd-tax-filing-expert" 2>/dev/null || true

echo "Success! youth-tax-calculator has been installed globally."
echo "Target Location: $TARGET_DIR"
echo "You can now ask Antigravity about Bangladesh student, intern, and employee tax filing in any project."
