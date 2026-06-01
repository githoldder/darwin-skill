#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { existsSync, rmSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const registryPath = join(__dirname, "..", "registry", "skillpacks.json");
const registry = JSON.parse(readFileSync(registryPath, "utf8"));

function printHelp() {
  console.log(`Darwin Skillpacks Installer

Usage:
  darwin-skillpacks list
  darwin-skillpacks install <name|all> [--target ./skills] [--force]

Examples:
  npx @githoldder/darwin-skillpacks list
  npx @githoldder/darwin-skillpacks install all --target ./skills
  npx @githoldder/darwin-skillpacks install 02-project-delivery --target ./skills
`);
}

function parseArgs(argv) {
  const args = {
    command: argv[2],
    name: argv[3],
    target: registry.default_target || "./skills",
    force: false
  };

  for (let i = 4; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--target") {
      args.target = argv[i + 1];
      i += 1;
    } else if (arg === "--force") {
      args.force = true;
    } else if (arg === "--help" || arg === "-h") {
      args.command = "help";
    }
  }

  return args;
}

function listSkillpacks() {
  for (const item of registry.skillpacks) {
    console.log(`${item.name.padEnd(24)} ${item.priority.padEnd(3)} ${item.scene}`);
  }
}

function ensureGit() {
  const result = spawnSync("git", ["--version"], { stdio: "ignore" });
  if (result.status !== 0) {
    console.error("git is required but was not found in PATH.");
    process.exit(1);
  }
}

function installOne(item, targetRoot, force) {
  const targetDir = resolve(targetRoot, item.name);
  mkdirSync(resolve(targetRoot), { recursive: true });

  if (existsSync(targetDir)) {
    if (!force) {
      console.log(`skip ${item.name}: ${targetDir} already exists`);
      return;
    }
    rmSync(targetDir, { recursive: true, force: true });
  }

  console.log(`install ${item.name} -> ${targetDir}`);
  const result = spawnSync("git", ["clone", "--depth", "1", item.url, targetDir], {
    stdio: "inherit"
  });

  if (result.status !== 0) {
    console.error(`failed to install ${item.name}`);
    process.exit(result.status || 1);
  }
}

function installSkillpacks(name, target, force) {
  ensureGit();

  if (!name) {
    console.error("missing skillpack name. Use `all` or one name from `list`.");
    process.exit(1);
  }

  const selected = name === "all"
    ? registry.skillpacks
    : registry.skillpacks.filter((item) => item.name === name || item.repo_name === name);

  if (selected.length === 0) {
    console.error(`unknown skillpack: ${name}`);
    console.error("Run `darwin-skillpacks list` to see available skillpacks.");
    process.exit(1);
  }

  for (const item of selected) {
    installOne(item, target, force);
  }
}

const args = parseArgs(process.argv);

if (!args.command || args.command === "help" || args.command === "--help" || args.command === "-h") {
  printHelp();
} else if (args.command === "list") {
  listSkillpacks();
} else if (args.command === "install") {
  installSkillpacks(args.name, args.target, args.force);
} else {
  console.error(`unknown command: ${args.command}`);
  printHelp();
  process.exit(1);
}

