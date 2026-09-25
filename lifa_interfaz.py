def obtener_html_interfaz():
    """Devuelve la interfaz web de LIFA como un documento autocontenido."""
    return r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
    <meta name="theme-color" content="#07080c">
    <meta name="color-scheme" content="dark">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="LIFA">
    <meta name="format-detection" content="telephone=no">
    <title>LIFA · Asistente personal</title>

    <style>
        :root {
            color-scheme: dark;
            --background: #07080c;
            --surface: rgba(19, 21, 29, 0.78);
            --line: rgba(255, 255, 255, 0.09);
            --text: #f6f7fb;
            --text-muted: #979ba9;
            --text-subtle: #6f7380;
            --purple: #9a7cff;
            --green: #6ee7b7;
            --red: #ff7c8f;
            --amber: #ffc875;
            --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", system-ui, sans-serif;
        }

        *, *::before, *::after {
            box-sizing: border-box;
        }

        html {
            width: 100%;
            height: 100%;
            background: var(--background);
            -webkit-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }

        body {
            width: 100%;
            height: 100%;
            margin: 0;
            overflow: hidden;
            background:
                radial-gradient(circle at 8% -8%, rgba(122, 86, 247, 0.19), transparent 34%),
                radial-gradient(circle at 100% 24%, rgba(63, 211, 165, 0.10), transparent 30%),
                var(--background);
            color: var(--text);
            font-family: var(--font);
            font-size: 16px;
            -webkit-font-smoothing: antialiased;
            overscroll-behavior: none;
        }

        button, textarea {
            font: inherit;
        }

        button {
            color: inherit;
            -webkit-tap-highlight-color: transparent;
            touch-action: manipulation;
        }

        .app-shell {
            position: relative;
            isolation: isolate;
            display: grid;
            grid-template-rows: auto minmax(0, 1fr) auto;
            width: 100%;
            height: 100vh;
            height: 100dvh;
            margin: 0 auto;
            overflow: hidden;
        }

        .app-shell::before {
            position: absolute;
            z-index: -1;
            top: 12%;
            left: 50%;
            width: 330px;
            height: 330px;
            border-radius: 50%;
            background: rgba(126, 91, 255, 0.055);
            filter: blur(72px);
            content: "";
            transform: translateX(-50%);
            pointer-events: none;
        }

        .app-header {
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: space-between;
            min-height: 66px;
            padding: calc(10px + env(safe-area-inset-top)) 17px 10px;
            border-bottom: 1px solid var(--line);
            background: rgba(7, 8, 12, 0.76);
            -webkit-backdrop-filter: blur(24px) saturate(145%);
            backdrop-filter: blur(24px) saturate(145%);
        }

        .brand {
            display: flex;
            min-width: 0;
            align-items: center;
            gap: 11px;
        }

        .brand-mark,
        .assistant-avatar {
            position: relative;
            display: grid;
            flex: 0 0 auto;
            place-items: center;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.13);
            background:
                radial-gradient(circle at 32% 28%, rgba(255, 255, 255, 0.27), transparent 23%),
                linear-gradient(145deg, #8d72ff 0%, #6445dc 52%, #4bd0a0 130%);
            box-shadow: 0 8px 24px rgba(103, 70, 221, 0.26), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }

        .brand-mark {
            width: 38px;
            height: 38px;
            border-radius: 13px;
        }

        .brand-mark svg,
        .assistant-avatar svg {
            width: 56%;
            height: 56%;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.20));
        }

        .brand-copy {
            min-width: 0;
        }

        .brand-name {
            margin: 0;
            font-size: 17px;
            font-weight: 720;
            line-height: 1.1;
            letter-spacing: 0.08em;
        }

        .brand-caption {
            margin: 4px 0 0;
            overflow: hidden;
            color: var(--text-muted);
            font-size: 11px;
            font-weight: 520;
            line-height: 1;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .connection {
            display: flex;
            flex: 0 0 auto;
            min-height: 34px;
            align-items: center;
            gap: 7px;
            padding: 0 11px;
            border: 1px solid var(--line);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.045);
            color: #b9bdc9;
            font-size: 12px;
            font-weight: 590;
            white-space: nowrap;
        }

        .connection-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 0 4px rgba(110, 231, 183, 0.08), 0 0 12px rgba(110, 231, 183, 0.65);
        }

        .connection.is-working .connection-dot {
            background: var(--purple);
            box-shadow: 0 0 0 4px rgba(154, 124, 255, 0.10), 0 0 12px rgba(154, 124, 255, 0.72);
            animation: statusPulse 1.5s ease-in-out infinite;
        }

        .connection.is-offline .connection-dot {
            background: var(--red);
            box-shadow: 0 0 0 4px rgba(255, 124, 143, 0.08);
        }

        .conversation {
            position: relative;
            overflow-x: hidden;
            overflow-y: auto;
            padding: 22px 15px 30px;
            scroll-behavior: smooth;
            scroll-padding-block: 24px;
            overscroll-behavior-y: contain;
            -webkit-overflow-scrolling: touch;
        }

        .conversation-inner {
            width: min(100%, 720px);
            min-height: 100%;
            margin: 0 auto;
        }

        .welcome {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: clamp(16px, 5vh, 48px) 9px 24px;
            text-align: center;
            animation: riseIn 0.55s cubic-bezier(.2, .75, .25, 1) both;
        }

        .lifa-orb {
            position: relative;
            display: grid;
            width: 78px;
            height: 78px;
            margin-bottom: 23px;
            place-items: center;
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 27px;
            background:
                radial-gradient(circle at 31% 24%, rgba(255, 255, 255, 0.34), transparent 22%),
                linear-gradient(145deg, #957aff 0%, #6747df 54%, #3db98f 125%);
            box-shadow:
                0 22px 55px rgba(104, 72, 227, 0.31),
                0 0 0 9px rgba(148, 121, 255, 0.045),
                inset 0 1px 0 rgba(255, 255, 255, 0.22);
        }

        .lifa-orb::after {
            position: absolute;
            inset: -17px;
            border: 1px solid rgba(148, 121, 255, 0.10);
            border-radius: 39px;
            content: "";
            animation: orbitGlow 4s ease-in-out infinite;
        }

        .lifa-orb svg {
            width: 38px;
            height: 38px;
            filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.20));
        }

        .eyebrow {
            margin: 0 0 9px;
            color: var(--green);
            font-size: 11px;
            font-weight: 720;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        .welcome h1 {
            max-width: 390px;
            margin: 0;
            font-size: clamp(29px, 8vw, 38px);
            font-weight: 730;
            line-height: 1.08;
            letter-spacing: -0.045em;
        }

        .welcome-description {
            max-width: 350px;
            margin: 12px 0 0;
            color: var(--text-muted);
            font-size: 15px;
            line-height: 1.48;
        }

        .suggestions {
            display: flex;
            width: 100%;
            margin-top: 23px;
            padding: 2px 1px 5px;
            gap: 9px;
            overflow-x: auto;
            scrollbar-width: none;
            scroll-snap-type: x proximity;
            -webkit-overflow-scrolling: touch;
        }

        .suggestions::-webkit-scrollbar {
            display: none;
        }

        .suggestion {
            display: inline-flex;
            flex: 0 0 auto;
            min-height: 44px;
            align-items: center;
            gap: 8px;
            padding: 0 14px;
            border: 1px solid var(--line);
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.045);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.035);
            color: #d6d8e1;
            font-size: 13px;
            font-weight: 580;
            scroll-snap-align: start;
        }

        .suggestion:active {
            background: rgba(255, 255, 255, 0.085);
            transform: scale(0.98);
        }

        .suggestion-icon {
            display: grid;
            width: 24px;
            height: 24px;
            place-items: center;
            border-radius: 8px;
            background: rgba(154, 124, 255, 0.13);
            color: #bba9ff;
        }

        .suggestion-icon svg {
            width: 14px;
            height: 14px;
        }

        .message {
            display: flex;
            width: 100%;
            margin-top: 18px;
            animation: messageIn 0.34s cubic-bezier(.2, .8, .25, 1) both;
        }

        .message--user {
            justify-content: flex-end;
            padding-left: 48px;
        }

        .message--assistant {
            align-items: flex-start;
            gap: 9px;
            padding-right: 24px;
        }

        .assistant-avatar {
            width: 31px;
            height: 31px;
            margin-top: 19px;
            border-radius: 11px;
            box-shadow: 0 7px 19px rgba(103, 70, 221, 0.20), inset 0 1px 0 rgba(255, 255, 255, 0.16);
        }

        .message-stack {
            min-width: 0;
            max-width: min(86%, 560px);
        }

        .message-author {
            margin: 0 0 6px 3px;
            color: var(--text-muted);
            font-size: 11px;
            font-weight: 650;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .bubble {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--line);
        }

        .message--user .bubble {
            max-width: min(88%, 530px);
            padding: 11px 14px 8px;
            border-color: rgba(187, 169, 255, 0.18);
            border-radius: 20px 20px 6px 20px;
            background: linear-gradient(145deg, #8063ee, #6749d5);
            box-shadow: 0 12px 27px rgba(86, 56, 190, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.13);
        }

        .message--assistant .bubble {
            padding: 14px 14px 10px;
            border-radius: 7px 20px 20px 20px;
            background: var(--surface);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.025);
            -webkit-backdrop-filter: blur(18px) saturate(135%);
            backdrop-filter: blur(18px) saturate(135%);
        }

        .bubble--error {
            border-color: rgba(255, 124, 143, 0.23) !important;
            background: linear-gradient(145deg, rgba(50, 25, 32, 0.92), rgba(25, 20, 27, 0.92)) !important;
        }

        .bubble--warning {
            border-color: rgba(255, 200, 117, 0.20) !important;
        }

        .message-text {
            margin: 0;
            overflow-wrap: anywhere;
            color: #f1f2f7;
            font-size: 15px;
            line-height: 1.48;
            white-space: pre-wrap;
        }

        .message--user .message-text {
            color: #fff;
        }

        .message-time {
            display: block;
            margin-top: 5px;
            color: rgba(255, 255, 255, 0.49);
            font-size: 10px;
            font-variant-numeric: tabular-nums;
            line-height: 1;
            text-align: right;
        }

        .result-heading {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 0 0 8px;
            gap: 12px;
        }

        .result-title {
            margin: 0;
            color: #fff;
            font-size: 13px;
            font-weight: 700;
            line-height: 1.25;
        }

        .result-badge {
            display: inline-flex;
            flex: 0 0 auto;
            align-items: center;
            gap: 5px;
            padding: 4px 7px;
            border-radius: 999px;
            background: rgba(110, 231, 183, 0.09);
            color: var(--green);
            font-size: 9px;
            font-weight: 760;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .result-badge::before {
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: currentColor;
            content: "";
        }

        .result-badge--weather {
            background: rgba(255, 200, 117, 0.1);
            color: #ffd58d;
        }

        .result-badge--weather::before {
            display: none;
        }

        .result-badge-icon {
            width: 14px;
            height: 14px;
            flex: 0 0 auto;
            overflow: visible;
        }

        .message--assistant .bubble--weather {
            border-color: rgba(255, 200, 117, 0.18);
            background:
                radial-gradient(circle at 100% 0%, rgba(255, 193, 94, 0.09), transparent 38%),
                var(--surface);
        }

        .bubble--error .result-badge {
            background: rgba(255, 124, 143, 0.09);
            color: var(--red);
        }

        .bubble--warning .result-badge {
            background: rgba(255, 200, 117, 0.09);
            color: var(--amber);
        }

        .detail-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            margin: 13px 0 1px;
            padding: 11px;
            gap: 10px;
            border: 1px solid rgba(255, 255, 255, 0.065);
            border-radius: 13px;
            background: rgba(255, 255, 255, 0.035);
        }

        .detail-item {
            min-width: 0;
            margin: 0;
        }

        .detail-label {
            margin: 0 0 3px;
            color: var(--text-subtle);
            font-size: 9px;
            font-weight: 720;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .detail-value {
            margin: 0;
            overflow-wrap: anywhere;
            color: #dfe1e9;
            font-size: 12px;
            font-weight: 570;
            line-height: 1.35;
        }

        .alert-list {
            display: grid;
            margin: 12px 0 1px;
            padding: 0;
            gap: 7px;
            list-style: none;
        }

        .alert-item {
            display: flex;
            align-items: flex-start;
            gap: 9px;
            padding: 10px;
            border: 1px solid rgba(255, 255, 255, 0.065);
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.035);
            color: #dfe1e9;
            font-size: 12px;
            line-height: 1.4;
        }

        .mail-dot {
            width: 7px;
            height: 7px;
            margin-top: 5px;
            flex: 0 0 auto;
            border-radius: 50%;
            background: var(--purple);
            box-shadow: 0 0 9px rgba(154, 124, 255, 0.55);
        }

        .retry-button {
            display: inline-flex;
            min-height: 37px;
            margin-top: 12px;
            align-items: center;
            gap: 7px;
            padding: 0 12px;
            border: 1px solid rgba(255, 124, 143, 0.24);
            border-radius: 12px;
            background: rgba(255, 124, 143, 0.085);
            color: #ffb2bd;
            font-size: 12px;
            font-weight: 660;
        }

        .retry-button:active {
            background: rgba(255, 124, 143, 0.15);
            transform: scale(0.98);
        }

        .typing-bubble {
            display: flex;
            min-height: 46px;
            align-items: center;
            gap: 11px;
        }

        .typing-dots {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .typing-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #ad93ff;
            animation: typing 1.2s ease-in-out infinite;
        }

        .typing-dot:nth-child(2) { animation-delay: 0.14s; }
        .typing-dot:nth-child(3) { animation-delay: 0.28s; }

        .typing-label {
            color: var(--text-muted);
            font-size: 12px;
            font-weight: 560;
        }

        .composer-area {
            z-index: 6;
            padding: 10px 12px calc(10px + env(safe-area-inset-bottom));
            border-top: 1px solid var(--line);
            background: linear-gradient(to bottom, rgba(7, 8, 12, 0.72), rgba(7, 8, 12, 0.94));
            -webkit-backdrop-filter: blur(26px) saturate(145%);
            backdrop-filter: blur(26px) saturate(145%);
        }

        .composer-form {
            display: flex;
            width: min(100%, 720px);
            min-height: 56px;
            margin: 0 auto;
            align-items: flex-end;
            gap: 8px;
            padding: 6px 6px 6px 15px;
            border: 1px solid rgba(255, 255, 255, 0.105);
            border-radius: 22px;
            background: rgba(25, 27, 36, 0.88);
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.23), inset 0 1px 0 rgba(255, 255, 255, 0.035);
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .composer-form:focus-within {
            border-color: rgba(157, 128, 255, 0.44);
            box-shadow: 0 14px 38px rgba(0, 0, 0, 0.25), 0 0 0 3px rgba(142, 110, 255, 0.075);
        }

        .command-input {
            width: 100%;
            min-height: 39px;
            max-height: 116px;
            margin: 0;
            padding: 9px 0 8px;
            resize: none;
            overflow-x: hidden;
            overflow-y: auto;
            border: 0;
            outline: 0;
            background: transparent;
            color: var(--text);
            caret-color: #ab92ff;
            font-size: 16px;
            line-height: 22px;
        }

        .command-input::placeholder {
            color: #707482;
            opacity: 1;
        }

        .send-button {
            display: grid;
            width: 44px;
            height: 44px;
            flex: 0 0 44px;
            place-items: center;
            border: 0;
            border-radius: 15px;
            background: linear-gradient(145deg, #9c80ff, #7050e8);
            box-shadow: 0 8px 20px rgba(100, 68, 214, 0.32), inset 0 1px 0 rgba(255, 255, 255, 0.20);
            transition: opacity 0.2s ease, transform 0.15s ease, filter 0.2s ease;
        }

        .send-button svg {
            width: 19px;
            height: 19px;
        }

        .send-button:not(:disabled):active {
            transform: scale(0.91);
        }

        .send-button:disabled {
            opacity: 0.33;
            box-shadow: none;
            filter: saturate(0.55);
        }

        button:focus-visible,
        textarea:focus-visible {
            outline: 2px solid #c3b4ff;
            outline-offset: 2px;
        }

        .visually-hidden {
            position: absolute !important;
            width: 1px !important;
            height: 1px !important;
            padding: 0 !important;
            margin: -1px !important;
            overflow: hidden !important;
            clip: rect(0, 0, 0, 0) !important;
            white-space: nowrap !important;
            border: 0 !important;
        }

        @keyframes riseIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes messageIn {
            from { opacity: 0; transform: translateY(8px) scale(0.985); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        @keyframes typing {
            0%, 60%, 100% { opacity: 0.35; transform: translateY(0); }
            30% { opacity: 1; transform: translateY(-4px); }
        }

        @keyframes statusPulse {
            0%, 100% { opacity: 0.55; transform: scale(0.88); }
            50% { opacity: 1; transform: scale(1); }
        }

        @keyframes orbitGlow {
            0%, 100% { opacity: 0.5; transform: scale(0.96) rotate(0deg); }
            50% { opacity: 1; transform: scale(1.04) rotate(3deg); }
        }

        @media (min-width: 760px) and (min-height: 720px) {
            body {
                padding: 18px;
            }

            .app-shell {
                max-width: 820px;
                height: calc(100dvh - 36px);
                border: 1px solid rgba(255, 255, 255, 0.09);
                border-radius: 32px;
                background: rgba(8, 9, 14, 0.78);
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.42);
            }

            .app-header {
                padding-top: 10px;
                border-radius: 32px 32px 0 0;
            }

            .composer-area {
                padding-bottom: 12px;
                border-radius: 0 0 32px 32px;
            }

            .suggestions {
                justify-content: center;
            }
        }

        @media (max-width: 370px) {
            .connection {
                padding-inline: 9px;
            }

            .connection-label {
                display: none;
            }

            .message--assistant {
                padding-right: 4px;
            }

            .message-stack {
                max-width: calc(100% - 40px);
            }

            .detail-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                scroll-behavior: auto !important;
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>

<body>
    <div class="app-shell">
        <header class="app-header">
            <div class="brand" aria-label="LIFA, asistente personal">
                <div class="brand-mark" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="none">
                        <path d="M7 5.5v8.2c0 2.65 1.65 4.8 4.55 4.8H17" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
                        <path d="M13.4 7.1c.8-1.25 2.15-2.05 3.7-2.1-.03 1.57-.8 2.95-2.04 3.77-1.12.73-2.48.88-3.52.54.18-.76.8-1.58 1.86-2.21Z" fill="#A7F3D0"/>
                    </svg>
                </div>
                <div class="brand-copy">
                    <p class="brand-name">LIFA</p>
                    <p class="brand-caption">Tu asistente personal</p>
                </div>
            </div>

            <div class="connection" id="connectionStatus" role="status" aria-live="polite">
                <span class="connection-dot" aria-hidden="true"></span>
                <span class="connection-label" id="connectionLabel">En línea</span>
            </div>
        </header>

        <main class="conversation" id="conversation" role="log" aria-label="Conversación con LIFA" aria-live="polite" aria-relevant="additions" aria-busy="false">
            <div class="conversation-inner" id="messageList">
                <section class="welcome" aria-labelledby="welcomeTitle">
                    <div class="lifa-orb" aria-hidden="true">
                        <svg viewBox="0 0 24 24" fill="none">
                            <path d="M7 4.5v9.1c0 3.05 1.9 5.4 5.15 5.4H18" stroke="white" stroke-width="2.15" stroke-linecap="round"/>
                            <path d="M13.3 6.8c.85-1.35 2.35-2.2 4.05-2.23-.05 1.7-.9 3.18-2.25 4.02-1.2.75-2.67.88-3.76.5.2-.8.86-1.64 1.96-2.29Z" fill="#A7F3D0"/>
                        </svg>
                    </div>
                    <p class="eyebrow">LIFA está lista</p>
                    <h1 id="welcomeTitle">¿Qué quieres resolver?</h1>
                    <p class="welcome-description">Organiza tus eventos y revisa lo importante desde una sola conversación.</p>

                    <div class="suggestions" aria-label="Comandos sugeridos">
                        <button class="suggestion" type="button" data-command="Revisa mis correos importantes">
                            <span class="suggestion-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3.5" y="5.5" width="17" height="13" rx="3"/>
                                    <path d="m5.5 8 6.5 4.8L18.5 8"/>
                                </svg>
                            </span>
                            Revisar correos
                        </button>

                        <button class="suggestion" type="button" data-command="Agenda una reunión mañana a las 10:00">
                            <span class="suggestion-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3.5" y="5" width="17" height="15" rx="3"/>
                                    <path d="M8 3.5v3M16 3.5v3M3.5 9.5h17"/>
                                </svg>
                            </span>
                            Agendar reunión
                        </button>

                        <button class="suggestion" type="button" data-command="Crea un evento para estudiar el viernes a las 18:00">
                            <span class="suggestion-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round">
                                    <path d="M12 5v14M5 12h14"/>
                                </svg>
                            </span>
                            Crear evento
                        </button>
                    </div>
                </section>
            </div>
        </main>

        <footer class="composer-area">
            <form class="composer-form" id="composerForm" novalidate>
                <label class="visually-hidden" for="commandInput">Escribe una instrucción para LIFA</label>
                <textarea
                    class="command-input"
                    id="commandInput"
                    name="command"
                    rows="1"
                    maxlength="2000"
                    placeholder="Escribe una instrucción…"
                    autocomplete="off"
                    autocapitalize="sentences"
                    enterkeyhint="send"
                    spellcheck="true"
                ></textarea>
                <button class="send-button" id="sendButton" type="submit" aria-label="Enviar instrucción" disabled>
                    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
                        <path d="M5 12h13M13 7l5 5-5 5" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </form>
        </footer>
    </div>

    <script>
        (() => {
            "use strict";

            const form = document.getElementById("composerForm");
            const input = document.getElementById("commandInput");
            const sendButton = document.getElementById("sendButton");
            const conversation = document.getElementById("conversation");
            const messageList = document.getElementById("messageList");
            const connectionStatus = document.getElementById("connectionStatus");
            const connectionLabel = document.getElementById("connectionLabel");
            const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

            let requestInProgress = false;
            let thinkingMessage = null;

            const iconMarkup = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 5.5v8.2c0 2.65 1.65 4.8 4.55 4.8H17" stroke="white" stroke-width="2.2" stroke-linecap="round"/><path d="M13.4 7.1c.8-1.25 2.15-2.05 3.7-2.1-.03 1.57-.8 2.95-2.04 3.77-1.12.73-2.48.88-3.52.54.18-.76.8-1.58 1.86-2.21Z" fill="#A7F3D0"/></svg>';

            function createElement(tag, className, text) {
                const element = document.createElement(tag);
                if (className) element.className = className;
                if (text !== undefined) element.textContent = text;
                return element;
            }

            function formatTime() {
                return new Intl.DateTimeFormat("es-CL", {
                    hour: "2-digit",
                    minute: "2-digit",
                    hour12: false
                }).format(new Date());
            }

            function scrollToLatest(immediate = false) {
                window.requestAnimationFrame(() => {
                    conversation.scrollTo({
                        top: conversation.scrollHeight,
                        behavior: immediate || reduceMotion.matches ? "auto" : "smooth"
                    });
                });
            }

            function resizeInput() {
                input.style.height = "auto";
                input.style.height = Math.min(input.scrollHeight, 116) + "px";
                input.style.overflowY = input.scrollHeight > 116 ? "auto" : "hidden";
            }

            function updateSendButton() {
                sendButton.disabled = requestInProgress || input.value.trim().length === 0;
            }

            function updateConnectionState() {
                connectionStatus.classList.remove("is-offline", "is-working");

                if (requestInProgress) {
                    connectionStatus.classList.add("is-working");
                    connectionLabel.textContent = "Procesando";
                } else if (!navigator.onLine) {
                    connectionStatus.classList.add("is-offline");
                    connectionLabel.textContent = "Sin conexión";
                } else {
                    connectionLabel.textContent = "En línea";
                }
            }

            function setLoading(isLoading) {
                requestInProgress = isLoading;
                conversation.setAttribute("aria-busy", String(isLoading));
                updateSendButton();
                updateConnectionState();
            }

            function appendUserMessage(text) {
                const message = createElement("article", "message message--user");
                const bubble = createElement("div", "bubble");
                const paragraph = createElement("p", "message-text", text);
                const time = createElement("time", "message-time", formatTime());
                time.dateTime = new Date().toISOString();

                bubble.append(paragraph, time);
                message.append(bubble);
                messageList.append(message);
                scrollToLatest();
            }

            function createAssistantAvatar() {
                const avatar = createElement("div", "assistant-avatar");
                avatar.setAttribute("aria-hidden", "true");
                avatar.innerHTML = iconMarkup;
                return avatar;
            }

            function appendThinkingMessage() {
                const message = createElement("article", "message message--assistant");
                message.setAttribute("role", "status");
                message.setAttribute("aria-label", "LIFA está pensando");

                const stack = createElement("div", "message-stack");
                const author = createElement("p", "message-author", "LIFA");
                const bubble = createElement("div", "bubble typing-bubble");
                const dots = createElement("span", "typing-dots");
                dots.setAttribute("aria-hidden", "true");

                for (let index = 0; index < 3; index += 1) {
                    dots.append(createElement("span", "typing-dot"));
                }

                bubble.append(dots, createElement("span", "typing-label", "LIFA está pensando…"));
                stack.append(author, bubble);
                message.append(createAssistantAvatar(), stack);
                messageList.append(message);
                thinkingMessage = message;
                scrollToLatest();
            }

            function removeThinkingMessage() {
                if (thinkingMessage) {
                    thinkingMessage.remove();
                    thinkingMessage = null;
                }
            }

            function stringValue(value) {
                if (typeof value === "string" && value.trim()) return value.trim();
                if (typeof value === "number" || typeof value === "boolean") return String(value);
                return "";
            }

            function pickText(source, keys) {
                if (!source || typeof source !== "object") return "";
                for (const key of keys) {
                    const value = stringValue(source[key]);
                    if (value) return value;
                }
                return "";
            }

            function detailToText(detail) {
                const direct = stringValue(detail);
                if (direct) return direct;

                if (Array.isArray(detail)) {
                    const messages = detail
                        .map((item) => pickText(item, ["msg", "mensaje", "message"]))
                        .filter(Boolean);
                    if (messages.length) return messages.join(" · ");
                }

                return "";
            }

            function readableListItem(item) {
                const direct = stringValue(item);
                if (direct) return direct;
                return pickText(item, ["asunto", "titulo", "mensaje", "message", "nombre"]);
            }

            function intentName(intent) {
                const labels = {
                    crear_evento: "Calendario",
                    revisar_correo: "Correo",
                    consultar_clima: "Clima",
                    consultar_mapa: "Mapas",
                    desconocido: "Consulta"
                };
                return labels[intent] || "LIFA";
            }

            function createResultBadge(label, icon) {
                const badge = createElement("span", "result-badge");

                if (icon === "weather") {
                    badge.classList.add("result-badge--weather");

                    const weatherIcon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                    weatherIcon.setAttribute("class", "result-badge-icon");
                    weatherIcon.setAttribute("viewBox", "0 0 24 24");
                    weatherIcon.setAttribute("fill", "none");
                    weatherIcon.setAttribute("aria-hidden", "true");
                    weatherIcon.innerHTML = `
                        <circle cx="8.5" cy="8" r="3" fill="currentColor" opacity=".9"/>
                        <path d="M8.5 2.5v1.4M8.5 12.1v1.4M3 8h1.4M12.6 8H14M4.6 4.1l1 1M11.4 10.9l1 1M12.4 4.1l-1 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                        <path d="M8.2 18.5h9.1a3.2 3.2 0 0 0 .2-6.4 4.8 4.8 0 0 0-9-1.2h-.3a3.8 3.8 0 1 0 0 7.6Z" fill="#171922" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>
                    `;

                    badge.append(weatherIcon);
                }

                badge.append(createElement("span", "", label));
                return badge;
            }

            function parseResponse(data, responseOK, statusCode) {
                const root = data && typeof data === "object" ? data : {};
                const action = root.accion_ejecutada && typeof root.accion_ejecutada === "object"
                    ? root.accion_ejecutada
                    : {};
                const analysis = root.analisis_ia && typeof root.analisis_ia === "object"
                    ? root.analisis_ia
                    : {};
                const parameters = analysis.parametros && typeof analysis.parametros === "object"
                    ? analysis.parametros
                    : {};

                const rootStatus = stringValue(root.status).toLowerCase();
                const actionStatus = stringValue(action.status).toLowerCase();
                const intent = stringValue(analysis.intent);
                const details = [];
                const items = [];
                let tone = "success";
                let title = "Respuesta de LIFA";
                let badge = intentName(intent);
                let icon = intent === "consultar_clima" ? "weather" : "";
                let text = "";

                if (!responseOK) {
                    tone = "error";
                    title = statusCode === 403 ? "Acceso no autorizado" : "No pude procesar la solicitud";
                    badge = "Error " + statusCode;
                    icon = "";
                    text = detailToText(root.detail)
                        || pickText(root, ["mensaje", "message", "error"])
                        || "El servidor no pudo completar la solicitud. Inténtalo nuevamente.";
                } else if (rootStatus === "error") {
                    tone = "error";
                    title = "No pude completar eso";
                    badge = "Error";
                    icon = "";
                    text = pickText(root, ["mensaje", "respuesta", "message", "error"])
                        || "Ocurrió un problema al procesar tu instrucción.";
                } else if (actionStatus === "error") {
                    tone = "error";
                    title = "La acción no se completó";
                    badge = intentName(intent);
                    text = pickText(action, ["mensaje", "respuesta", "message", "error"])
                        || "Pude entender la solicitud, pero no fue posible ejecutar la acción.";
                } else if (Array.isArray(action.alertas)) {
                    const alerts = action.alertas.map(readableListItem).filter(Boolean);
                    title = alerts.length ? "Correos importantes" : "Bandeja revisada";
                    badge = "Correo";
                    text = alerts.length
                        ? "Encontré " + alerts.length + (alerts.length === 1 ? " correo importante" : " correos importantes") + " sin leer."
                        : "Revisé tu bandeja y no encontré correos importantes sin leer.";
                    items.push(...alerts);
                } else {
                    text = pickText(action, ["mensaje", "respuesta", "message", "texto", "resultado", "output"])
                        || pickText(root, ["mensaje", "respuesta", "response", "message", "texto", "resultado", "result", "output"])
                        || pickText(analysis, ["mensaje", "respuesta", "response", "message", "texto", "resultado"]);

                    if (!text) {
                        text = "Procesé tu solicitud, pero el servidor no entregó un detalle para mostrar.";
                    }
                }

                const actionMessage = pickText(action, ["mensaje", "respuesta", "message", "texto", "resultado", "output"]);
                const usesGenericPresentation = ![
                    "crear_evento",
                    "revisar_correo",
                    "consultar_clima",
                    "desconocido"
                ].includes(intent);

                if (usesGenericPresentation && actionMessage && tone !== "error") {
                    tone = "success";
                    title = "Respuesta de LIFA";
                    badge = "LIFA";
                    icon = "";
                } else if (intent === "consultar_clima" && tone === "success") {
                    title = "Clima actual";
                    badge = "Clima";
                    icon = "weather";
                } else if (actionStatus === "warning" && tone !== "error") {
                    tone = "warning";
                    title = "Necesito un poco más de contexto";
                    badge = "Aviso";
                } else if (intent === "crear_evento" && tone === "success") {
                    title = "Evento guardado";
                    badge = "Calendario";

                    const eventTitle = pickText(parameters, ["titulo", "title", "nombre"]);
                    const date = pickText(parameters, ["fecha", "date"]);
                    const time = pickText(parameters, ["hora", "time"]);
                    const place = pickText(parameters, ["lugar", "ubicacion", "location"]);
                    const notes = pickText(parameters, ["notas", "descripcion", "description"]);

                    if (eventTitle) details.push({ label: "Evento", value: eventTitle });
                    if (date) details.push({ label: "Fecha", value: date });
                    if (time) details.push({ label: "Hora", value: time });
                    if (place) details.push({ label: "Lugar", value: place });
                    if (notes) details.push({ label: "Notas", value: notes });
                }

                return { tone, title, badge, icon, text, details, items };
            }

            function appendAssistantMessage(viewModel, originalCommand) {
                const message = createElement("article", "message message--assistant");
                const stack = createElement("div", "message-stack");
                const author = createElement("p", "message-author", "LIFA");
                const bubble = createElement("div", "bubble");

                if (viewModel.tone === "error") bubble.classList.add("bubble--error");
                if (viewModel.tone === "warning") bubble.classList.add("bubble--warning");
                if (viewModel.icon === "weather" && viewModel.tone !== "error") {
                    bubble.classList.add("bubble--weather");
                }

                const heading = createElement("div", "result-heading");
                heading.append(
                    createElement("p", "result-title", viewModel.title),
                    createResultBadge(viewModel.badge, viewModel.icon)
                );

                bubble.append(heading, createElement("p", "message-text", viewModel.text));

                if (viewModel.details.length) {
                    const detailGrid = createElement("dl", "detail-grid");
                    viewModel.details.forEach(({ label, value }) => {
                        const item = createElement("div", "detail-item");
                        item.append(
                            createElement("dt", "detail-label", label),
                            createElement("dd", "detail-value", value)
                        );
                        detailGrid.append(item);
                    });
                    bubble.append(detailGrid);
                }

                if (viewModel.items.length) {
                    const list = createElement("ul", "alert-list");
                    viewModel.items.forEach((itemText) => {
                        const item = createElement("li", "alert-item");
                        item.append(createElement("span", "mail-dot"), createElement("span", "", itemText));
                        list.append(item);
                    });
                    bubble.append(list);
                }

                if (viewModel.tone === "error") {
                    const retry = createElement("button", "retry-button", "Intentar de nuevo");
                    retry.type = "button";
                    retry.addEventListener("click", () => {
                        if (requestInProgress) return;
                        input.value = originalCommand;
                        resizeInput();
                        updateSendButton();
                        form.requestSubmit();
                    });
                    bubble.append(retry);
                }

                const time = createElement("time", "message-time", formatTime());
                time.dateTime = new Date().toISOString();
                bubble.append(time);
                stack.append(author, bubble);
                message.append(createAssistantAvatar(), stack);
                messageList.append(message);
                scrollToLatest();
            }

            async function enviarComando(valorDelInput) {
                appendUserMessage(valorDelInput);
                appendThinkingMessage();
                setLoading(true);

                const controller = new AbortController();
                const timeout = window.setTimeout(() => controller.abort(), 45000);

                try {
                    const response = await fetch('/procesar', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-API-Key': 'LeonoLuna2004'
                        },
                        body: JSON.stringify({ texto: valorDelInput }),
                        signal: controller.signal
                    });

                    const data = await response.json();
                    removeThinkingMessage();
                    appendAssistantMessage(parseResponse(data, response.ok, response.status), valorDelInput);
                } catch (error) {
                    removeThinkingMessage();

                    const timedOut = error && error.name === "AbortError";
                    appendAssistantMessage({
                        tone: "error",
                        title: timedOut ? "LIFA tardó demasiado" : "No pude conectar con LIFA",
                        badge: "Conexión",
                        text: timedOut
                            ? "El servidor no respondió a tiempo. Comprueba la conexión e inténtalo nuevamente."
                            : "No recibí una respuesta válida del servidor. Revisa tu conexión e inténtalo de nuevo.",
                        details: [],
                        items: []
                    }, valorDelInput);
                } finally {
                    window.clearTimeout(timeout);
                    setLoading(false);
                }
            }

            form.addEventListener("submit", (event) => {
                event.preventDefault();
                const valorDelInput = input.value.trim();
                if (!valorDelInput || requestInProgress) return;

                input.value = "";
                resizeInput();
                updateSendButton();
                enviarComando(valorDelInput);
            });

            input.addEventListener("input", () => {
                resizeInput();
                updateSendButton();
            });

            input.addEventListener("keydown", (event) => {
                if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
                    event.preventDefault();
                    form.requestSubmit();
                }
            });

            input.addEventListener("focus", () => {
                window.setTimeout(() => scrollToLatest(true), 260);
            });

            document.querySelectorAll("[data-command]").forEach((button) => {
                button.addEventListener("click", () => {
                    input.value = button.dataset.command || "";
                    resizeInput();
                    updateSendButton();
                    input.focus();
                    input.setSelectionRange(input.value.length, input.value.length);
                });
            });

            window.addEventListener("online", updateConnectionState);
            window.addEventListener("offline", updateConnectionState);
            window.addEventListener("pageshow", updateConnectionState);

            resizeInput();
            updateSendButton();
            updateConnectionState();
        })();
    </script>
</body>
</html>
"""
