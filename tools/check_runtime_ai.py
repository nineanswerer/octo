#!/usr/bin/env python3
"""
check_runtime_ai.py — 检查 OctoSense 宿主 AI 配置状态

用法: python check_runtime_ai.py --core-dir <OCTOS_APP_CORE_DIR>

参数:
  --core-dir  必选。指向 OctoSense 核心数据目录的绝对路径。
              该目录下应有 profiles/_main.json 文件。

输出:
  JSON 格式状态报告，固定字段。

退出码:
  0 - CONFIGURED_UNTESTED (已配置有效 primary)
  2 - NO_PROFILE / INVALID_PROFILE / DISABLED_PROFILE / NO_PRIMARY
"""

import argparse
import json
import sys
import os


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check OctoSense runtime AI configuration status."
    )
    parser.add_argument(
        "--core-dir",
        required=True,
        help="Path to OCTOS_APP_CORE_DIR (must be absolute).",
    )
    args = parser.parse_args()

    core_dir = os.path.abspath(args.core_dir)
    profile_path = os.path.join(core_dir, "profiles", "_main.json")

    result = {
        "profile_exists": False,
        "profile_parseable": False,
        "profile_enabled": None,
        "primary_configured": False,
        "fallback_count": 0,
        "status": "UNKNOWN",
    }

    # Check profile existence
    if not os.path.isfile(profile_path):
        result["status"] = "NO_PROFILE"
        print(json.dumps(result))
        sys.exit(2)

    result["profile_exists"] = True

    # Read and parse profile (accept UTF-8 BOM)
    try:
        with open(profile_path, "r", encoding="utf-8-sig") as f:
            profile = json.load(f)
    except (json.JSONDecodeError, UnicodeError, OSError):
        result["status"] = "INVALID_PROFILE"
        print(json.dumps(result))
        sys.exit(2)

    # Validate structure: must be a dict
    if not isinstance(profile, dict):
        result["status"] = "INVALID_PROFILE"
        print(json.dumps(result))
        sys.exit(2)

    result["profile_parseable"] = True

    # Check enabled flag (must be exactly True, not truthiness)
    enabled = profile.get("enabled")
    result["profile_enabled"] = enabled is True
    if enabled is not True:
        result["status"] = "DISABLED_PROFILE"
        print(json.dumps(result))
        sys.exit(2)

    result["profile_enabled"] = True

    # Navigate to config.llm
    config = profile.get("config")
    if not isinstance(config, dict):
        result["status"] = "NO_PRIMARY"
        print(json.dumps(result))
        sys.exit(2)

    llm = config.get("llm")
    if not isinstance(llm, dict):
        result["status"] = "NO_PRIMARY"
        print(json.dumps(result))
        sys.exit(2)

    # Check primary — must be a dict with nonempty family_id and model_id
    primary = llm.get("primary")
    if isinstance(primary, dict):
        family_id = primary.get("family_id")
        model_id = primary.get("model_id")
        if isinstance(family_id, str) and family_id and isinstance(model_id, str) and model_id:
            result["primary_configured"] = True

    if not result["primary_configured"]:
        result["status"] = "NO_PRIMARY"
        print(json.dumps(result))
        sys.exit(2)

    # Count valid fallbacks: dict entries with nonempty family and model
    fallbacks = llm.get("fallbacks")
    count = 0
    if isinstance(fallbacks, list):
        for fb in fallbacks:
            if isinstance(fb, dict):
                f = fb.get("family_id")
                m = fb.get("model_id")
                if isinstance(f, str) and f and isinstance(m, str) and m:
                    count += 1

    result["fallback_count"] = count
    result["status"] = "CONFIGURED_UNTESTED"
    print(json.dumps(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
