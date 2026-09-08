#!/usr/bin/env bash
set -e

# Generates a 32-byte (64-character) secure hex key.
# Output: Standard output string containing the generated key.
generate_cookie() {
    openssl rand -hex 32
}

main() {
    if [ -f .env ]; then
        echo ".env already exists, skipping."
        exit 0
    fi

    cp .env.example .env

    local cookie
    cookie=$(generate_cookie)

    sed -i.bak "s|^EMQX_NODE__COOKIE=.*|EMQX_NODE__COOKIE=${cookie}|" .env
    rm -f .env.bak

    echo ".env created with a fresh cookie."
}

main "$@"
