#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_HOME="$HOME/.codex"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

log() {
  printf '[setup] %s\n' "$*"
}

warn() {
  printf '[setup][warn] %s\n' "$*" >&2
}

ensure_cmd() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    warn "缺少命令: $cmd"
    return 1
  fi
}

install_codex() {
  if command -v codex >/dev/null 2>&1; then
    log "检测到 codex: $(codex --version 2>/dev/null || echo 'unknown version')"
    log "尝试更新 codex 到最新版本..."
  else
    log "未检测到 codex，准备安装..."
  fi

  npm install -g @openai/codex
  log "codex 安装完成: $(codex --version 2>/dev/null || echo 'installed')"
}

backup_existing_codex_home() {
  if [ -e "$TARGET_HOME" ] && [ ! -L "$TARGET_HOME" ]; then
    local backup_path="${TARGET_HOME}.backup.${TIMESTAMP}"
    log "发现已有目录 $TARGET_HOME，先备份到 $backup_path"
    mv "$TARGET_HOME" "$backup_path"
  elif [ -L "$TARGET_HOME" ]; then
    local current_link
    current_link="$(readlink "$TARGET_HOME" || true)"
    log "$TARGET_HOME 当前是软链接 -> $current_link"
  fi
}

link_repo_as_codex_home() {
  if [ -L "$TARGET_HOME" ]; then
    rm "$TARGET_HOME"
  elif [ -e "$TARGET_HOME" ]; then
    warn "$TARGET_HOME 仍然存在且不是软链接，已中止。"
    return 1
  fi

  ln -s "$REPO_ROOT" "$TARGET_HOME"
  log "已将当前仓库设置为 Codex Home: $TARGET_HOME -> $REPO_ROOT"
}

print_next_steps() {
  cat <<MSG

✅ 初始化完成

- Codex Home: $TARGET_HOME
- 当前仓库: $REPO_ROOT

建议执行：
1) 重新打开终端
2) 运行: codex --version
3) 运行: ls -la "$TARGET_HOME"

如果你希望用环境变量明确指定，也可以在 shell 配置里加：
export CODEX_HOME="$TARGET_HOME"
MSG
}

main() {
  ensure_cmd npm
  install_codex
  backup_existing_codex_home
  link_repo_as_codex_home
  print_next_steps
}

main "$@"
