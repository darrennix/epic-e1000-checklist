# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose
This repository contains JSON-formatted aircraft procedure checklists for the Epic E1000 GX aircraft.

## File Structure
- `*.json` files contain procedure checklists in a structured JSON format
- `*.pdf` files contain reference documentation for procedures

## Code Style Guidelines
- Maintain consistent JSON indentation (2 spaces)
- Keep JSON properties alphabetized within objects
- Ensure proper nesting of groups > checklists > entries
- Follow existing naming conventions for checklist entry types
- Preserve formatting for capitalized text in procedure steps
- Maintain existing justification specifications (center, indent1)
- Use camelCase for property names

## Validation
- Ensure all JSON files are valid (well-formed)
- Verify all required fields are present (text, type, response where applicable)
- Check for proper entry type values ("Challenge", "MemoryItem", "Warning", etc.)

## Common Operations
- Use `jq` for JSON validation: `jq . filename.json`
- Format JSON: `jq . filename.json > temp.json && mv temp.json filename.json`
- Check references between checklists in cross-references