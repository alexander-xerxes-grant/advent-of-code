RED := '\033[0;31m'
RESET := '\033[0m'

@_default:
    just --list

_echo_err +msg:
    #!/usr/bin/env bash
    echo -e >&2 "{{ RED }}ERROR{{ RESET }}: {{ msg }}"

_get_day d:
    #!/usr/bin/env bash
    [[ ! "{{ d }}" =~ ^(0?[1-9]|1[0-9]|2[0-5])$ ]] && just _echo_err "Invalid day: {{ d }}" && exit
    DAY=$([[ {{ d }} =~ ^[1-9]$ ]] && echo "0{{ d }}" || echo "{{ d }}")
    [[ -e "day${DAY}" ]] && just _echo_err "Day already exists at ./day${DAY}. Aborting" && exit

    echo "$DAY"

# Create a new folder for the provided day
create d:
    #!/usr/bin/env bash
    DAY="$(just _get_day {{ d }})" && [[ -z "$DAY" ]] && exit

    # Enable for recursive globbing
    shopt -s globstar

    echo "Creating folder for $DAY..."

    for origin in template/*; do
    target="${origin/#template\//}/day$DAY"

    [[ -e "$target" ]] && just _echo_err "Target already exists. Aborting" && exit

    if [[ -d "$origin" && ! -L "$origin" ]]; then
        mkdir -p "$target"

        for sub_origin in "${origin}"/**/*; do
        sub_target="${sub_origin/#$origin/$target}"

        if [[ -d "$sub_origin" ]]; then
            mkdir -p "$sub_target"
        fi
        done

        for sub_origin in "${origin}"/**/*; do
        sub_target="${sub_origin/#$origin/$target}"

        if [[ ! -d "$sub_origin" ]]; then
            sed 's/dayDAY/day'"$DAY"'/g' "$sub_origin" > "$sub_target"
        fi
        done
    fi
    done
