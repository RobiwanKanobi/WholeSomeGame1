from html import escape
from pathlib import Path


WIDTH = 1232
HEIGHT = 706


def common_defs(start: str, end: str, accent: str) -> str:
    return f"""    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{start}" />
      <stop offset="100%" stop-color="{end}" />
    </linearGradient>
    <radialGradient id="bloom" cx="72%" cy="42%" r="52%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.56" />
      <stop offset="100%" stop-color="{accent}" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#162232" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#0b121d" stop-opacity="0.78" />
    </linearGradient>
    <radialGradient id="fog" cx="52%" cy="58%" r="78%">
      <stop offset="56%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#05070a" stop-opacity="0.38" />
    </radialGradient>
    <filter id="shadow" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#04101b" flood-opacity="0.35" />
    </filter>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
"""


def title_block(lines: list[str], x: int = 64, y: int = 456, width: int = 410) -> str:
    safe_lines = [escape(line) for line in lines]
    height = 74 + len(safe_lines) * 62
    line_text = []
    current_y = y + 78

    for line in safe_lines:
        line_text.append(
            f'  <text x="{x + 28}" y="{current_y}" font-family="Inter, Arial, sans-serif" '
            f'font-size="56" font-weight="800" fill="#fff9ef" paint-order="stroke" '
            f'stroke="rgba(0,0,0,0.22)" stroke-width="8">{line}</text>'
        )
        current_y += 58

    return "\n".join(
        [
            f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="28" fill="url(#panel)" stroke="rgba(255,255,255,0.24)" />',
            f'  <rect x="{x + 28}" y="{y + 22}" width="118" height="8" rx="4" fill="rgba(255,234,188,0.86)" />',
            *line_text,
        ]
    )


def wrap_svg(title: str, description: str, title_lines: list[str], defs: str, body: str) -> str:
    safe_title = escape(title)
    safe_description = escape(description)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title>{safe_title}</title>
  <desc>{safe_description}</desc>
  <defs>
{defs}
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="32" fill="url(#bg)" />
  <rect x="16" y="16" width="{WIDTH - 32}" height="{HEIGHT - 32}" rx="28" fill="none" stroke="rgba(255,255,255,0.24)" />
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bloom)" />
{body}
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#fog)" />
{title_block(title_lines)}
</svg>
"""


def loom_and_lantern() -> str:
    defs = common_defs("#25315b", "#f09361", "#ffd58d")
    body = """
  <circle cx="1056" cy="118" r="58" fill="#fff1c8" opacity="0.46" />
  <path d="M0 432 C154 396 306 438 476 404 C660 370 858 432 1038 396 C1132 378 1194 372 1232 366 V706 H0 Z" fill="#314978" />
  <path d="M0 510 C168 478 344 542 516 510 C686 478 856 536 1036 504 C1124 490 1188 484 1232 478 V706 H0 Z" fill="#44395c" />
  <path d="M0 568 C174 542 362 588 536 562 C708 536 894 592 1082 554 C1156 540 1210 532 1232 526 V706 H0 Z" fill="#2f2941" />
  <rect x="790" y="132" width="16" height="338" rx="8" fill="#35263d" />
  <rect x="948" y="132" width="16" height="338" rx="8" fill="#35263d" />
  <path d="M784 140 C826 72 926 72 972 140" fill="none" stroke="#3f2c44" stroke-width="16" stroke-linecap="round" />
  <rect x="846" y="180" width="64" height="164" rx="30" fill="#ffcb73" filter="url(#glow)" />
  <rect x="860" y="194" width="36" height="138" rx="18" fill="#fff6d6" opacity="0.8" />
  <path d="M768 218 C1010 214 1094 314 1176 398" fill="none" stroke="#ffd584" stroke-width="10" stroke-linecap="round" filter="url(#glow)" />
  <path d="M774 248 C986 260 1070 344 1140 424" fill="none" stroke="#95e7db" stroke-width="8" stroke-linecap="round" />
  <path d="M780 276 C962 300 1038 378 1102 456" fill="none" stroke="#f4a1ba" stroke-width="8" stroke-linecap="round" />
  <rect x="824" y="166" width="8" height="188" fill="#f37e57" />
  <rect x="850" y="166" width="8" height="188" fill="#f6c161" />
  <rect x="876" y="166" width="8" height="188" fill="#84e2d8" />
  <rect x="902" y="166" width="8" height="188" fill="#f4adc3" />
  <path d="M126 560 h82 v82 h-82 z" fill="#6b5760" />
  <path d="M228 524 h94 v118 h-94 z" fill="#7f6970" />
  <path d="M342 548 h108 v94 h-108 z" fill="#8f7477" />
  <path d="M472 506 h92 v136 h-92 z" fill="#75616b" />
  <polygon points="126,560 167,522 208,560" fill="#48384f" />
  <polygon points="228,524 275,480 322,524" fill="#533e59" />
  <polygon points="342,548 396,506 450,548" fill="#584260" />
  <polygon points="472,506 518,466 564,506" fill="#523d59" />
  <circle cx="278" cy="564" r="8" fill="#ffd99f" filter="url(#glow)" />
  <circle cx="518" cy="552" r="9" fill="#ffd99f" filter="url(#glow)" />
"""
    return wrap_svg("Loom & Lantern", "Steam capsule concept art with glowing lantern loom and stitched twilight thread", ["Loom", "& Lantern"], defs, body)


def starlight_apiary() -> str:
    defs = common_defs("#14254a", "#2a5a74", "#8befff")
    body = """
  <circle cx="1000" cy="130" r="70" fill="#f8efc3" opacity="0.32" />
  <path d="M0 504 C194 468 358 526 546 498 C706 474 888 526 1066 494 C1148 480 1206 470 1232 464 V706 H0 Z" fill="#11253f" />
  <path d="M0 560 C208 528 376 578 560 548 C724 522 912 578 1080 548 C1156 534 1208 526 1232 520 V706 H0 Z" fill="#163550" />
  <path d="M840 154 L888 126 L924 164 L970 130 L1010 176 L1058 144" fill="none" stroke="#90ebff" stroke-width="6" stroke-linecap="round" />
  <circle cx="840" cy="154" r="9" fill="#90ebff" filter="url(#glow)" />
  <circle cx="888" cy="126" r="7" fill="#90ebff" filter="url(#glow)" />
  <circle cx="924" cy="164" r="8" fill="#90ebff" filter="url(#glow)" />
  <circle cx="970" cy="130" r="7" fill="#90ebff" filter="url(#glow)" />
  <circle cx="1010" cy="176" r="8" fill="#90ebff" filter="url(#glow)" />
  <circle cx="1058" cy="144" r="7" fill="#90ebff" filter="url(#glow)" />
  <path d="M706 210 C746 166 842 156 896 202 L914 326 C918 380 876 420 822 420 H768 C714 420 672 380 676 326 Z" fill="rgba(255,255,255,0.18)" stroke="rgba(255,255,255,0.38)" stroke-width="8" />
  <path d="M732 242 h126 v46 c0 52 -28 76 -64 76 c-36 0 -62 -24 -62 -76 z" fill="#f0b764" filter="url(#glow)" />
  <rect x="776" y="208" width="38" height="34" rx="12" fill="#ffe6b2" />
  <path d="M518 300 h126 l20 26 v104 l-20 22 h-126 l-20 -22 v-104 z" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.28)" stroke-width="6" />
  <path d="M536 330 h90 M536 368 h90 M536 406 h90" stroke="rgba(255,255,255,0.22)" stroke-width="14" stroke-linecap="round" />
  <ellipse cx="938" cy="468" rx="26" ry="12" fill="#82edff" />
  <ellipse cx="988" cy="430" rx="24" ry="11" fill="#82edff" />
  <ellipse cx="1040" cy="474" rx="28" ry="12" fill="#82edff" />
  <ellipse cx="226" cy="592" rx="84" ry="34" fill="#2b615d" />
  <ellipse cx="312" cy="564" rx="74" ry="30" fill="#366d66" />
  <ellipse cx="388" cy="598" rx="66" ry="26" fill="#2b5753" />
  <path d="M146 624 C260 566 368 568 470 620" fill="none" stroke="#53cda7" stroke-width="10" stroke-linecap="round" />
  <path d="M192 644 C284 596 396 600 510 644" fill="none" stroke="#f6a3c5" stroke-width="10" stroke-linecap="round" />
"""
    return wrap_svg("Starlight Apiary", "Steam capsule concept art with honey jar focal point and glowing bee constellations", ["Starlight", "Apiary"], defs, body)


def tide_painter() -> str:
    defs = common_defs("#ffd7b4", "#4489bf", "#fff0c7")
    body = """
  <circle cx="1008" cy="118" r="78" fill="#fff0c9" opacity="0.56" />
  <path d="M0 366 C142 340 320 372 480 346 C620 324 752 350 916 324 C1040 304 1138 314 1232 304 V706 H0 Z" fill="#8fd1ef" />
  <path d="M0 442 C156 420 332 456 492 430 C644 404 802 444 962 420 C1082 402 1168 408 1232 400 V706 H0 Z" fill="#5ca7d6" />
  <path d="M0 528 C154 514 336 548 522 520 C698 494 862 540 1018 512 C1110 498 1176 500 1232 492 V706 H0 Z" fill="#f0c89d" />
  <path d="M0 598 C166 584 336 626 526 606 C714 586 874 632 1028 606 C1114 592 1178 592 1232 586 V706 H0 Z" fill="#f5dfb9" />
  <path d="M246 540 C404 432 602 404 804 450 C918 476 1022 520 1114 576" fill="none" stroke="#ff8b66" stroke-width="24" stroke-linecap="round" filter="url(#glow)" />
  <path d="M256 564 C432 470 630 452 828 500 C920 522 1012 568 1088 616" fill="none" stroke="#95f4de" stroke-width="10" stroke-linecap="round" />
  <path d="M762 374 C878 382 972 426 1056 498" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="12" stroke-linecap="round" />
  <path d="M804 408 C916 420 996 462 1070 528" fill="none" stroke="rgba(255,255,255,0.42)" stroke-width="8" stroke-linecap="round" />
  <rect x="196" y="498" width="14" height="140" rx="7" fill="#61473d" transform="rotate(-22 196 498)" />
  <path d="M120 634 C156 590 198 558 246 546 C266 542 278 560 270 578 C252 618 214 642 166 650 Z" fill="#1f4854" />
  <circle cx="388" cy="616" r="16" fill="#f5b58c" />
  <circle cx="438" cy="596" r="18" fill="#f5b58c" />
  <circle cx="486" cy="628" r="16" fill="#f5b58c" />
"""
    return wrap_svg("The Tide Painter", "Steam capsule concept art with dramatic brushstroke wave and reflective sunrise beach", ["The Tide", "Painter"], defs, body)


def clockmakers_conservatory() -> str:
    defs = common_defs("#90c39e", "#314d54", "#ffd486")
    body = """
  <path d="M0 522 C196 472 346 540 544 490 C726 446 890 522 1078 482 C1142 468 1194 460 1232 454 V706 H0 Z" fill="#233d43" />
  <path d="M166 144 V552 C166 188 204 152 250 152 H1082 C1128 152 1166 188 1166 234 V552" fill="none" stroke="rgba(255,255,255,0.24)" stroke-width="10" />
  <path d="M308 168 V552 M622 152 V552 M932 168 V552" stroke="rgba(255,255,255,0.14)" stroke-width="4" />
  <path d="M894 182 C856 286 818 358 748 486" fill="none" stroke="rgba(255,241,190,0.34)" stroke-width="18" stroke-linecap="round" />
  <circle cx="846" cy="354" r="122" fill="rgba(255,212,134,0.2)" />
  <circle cx="846" cy="354" r="88" fill="none" stroke="#d5b06a" stroke-width="16" />
  <circle cx="846" cy="354" r="28" fill="#d5b06a" />
  <circle cx="846" cy="286" r="20" fill="#d5b06a" />
  <circle cx="906" cy="322" r="20" fill="#d5b06a" />
  <circle cx="906" cy="388" r="20" fill="#d5b06a" />
  <circle cx="846" cy="424" r="20" fill="#d5b06a" />
  <circle cx="786" cy="388" r="20" fill="#d5b06a" />
  <circle cx="786" cy="322" r="20" fill="#d5b06a" />
  <rect x="932" y="232" width="12" height="234" rx="6" fill="#d9c094" />
  <circle cx="938" cy="490" r="34" fill="#d9c094" />
  <path d="M522 552 C542 464 586 406 650 350" fill="none" stroke="#5a8f5e" stroke-width="22" stroke-linecap="round" />
  <path d="M650 350 C610 328 574 298 544 254" fill="none" stroke="#82d886" stroke-width="14" stroke-linecap="round" />
  <path d="M676 316 C716 294 756 264 804 220" fill="none" stroke="#82d886" stroke-width="14" stroke-linecap="round" />
  <circle cx="650" cy="350" r="24" fill="#f7d68b" filter="url(#glow)" />
  <circle cx="612" cy="286" r="18" fill="#f7d68b" />
  <circle cx="812" cy="218" r="18" fill="#f7d68b" />
"""
    return wrap_svg("Clockmaker's Conservatory", "Steam capsule concept art with giant brass clock flower and greenhouse silhouettes", ["Clockmaker's", "Conservatory"], defs, body)


def song_of_the_rootbound() -> str:
    defs = common_defs("#183052", "#2c5a46", "#9ef6c6")
    body = """
  <path d="M0 504 C190 462 356 520 538 484 C722 448 898 532 1088 492 C1158 476 1208 468 1232 462 V706 H0 Z" fill="#153147" />
  <path d="M0 570 C200 536 380 584 560 548 C736 516 920 588 1104 556 C1166 544 1210 538 1232 532 V706 H0 Z" fill="#1f423d" />
  <ellipse cx="260" cy="364" rx="36" ry="164" fill="#20402f" />
  <ellipse cx="1028" cy="344" rx="42" ry="186" fill="#1f3d30" />
  <path d="M742 190 C828 190 890 246 890 338 C890 430 830 492 742 492 C654 492 594 430 594 338 C594 246 656 190 742 190 Z" fill="#5f4734" filter="url(#shadow)" />
  <circle cx="742" cy="338" r="82" fill="#2b221c" />
  <path d="M650 338 C690 324 794 318 834 338" fill="none" stroke="#f0d38e" stroke-width="12" stroke-linecap="round" />
  <path d="M650 372 C694 358 792 354 836 372" fill="none" stroke="#f0d38e" stroke-width="10" stroke-linecap="round" />
  <rect x="720" y="118" width="18" height="332" rx="9" fill="#d7bb86" />
  <circle cx="728" cy="116" r="34" fill="#f0bc92" />
  <path d="M564 556 C654 508 736 490 832 490 C950 490 1034 528 1122 588" fill="none" stroke="rgba(160,249,205,0.68)" stroke-width="10" stroke-linecap="round" />
  <path d="M520 598 C636 532 756 522 874 532 C972 540 1060 576 1140 626" fill="none" stroke="rgba(160,249,205,0.42)" stroke-width="8" stroke-linecap="round" />
  <circle cx="932" cy="512" r="12" fill="#9ef6c6" filter="url(#glow)" />
  <circle cx="984" cy="544" r="12" fill="#9ef6c6" filter="url(#glow)" />
  <circle cx="1044" cy="572" r="12" fill="#9ef6c6" filter="url(#glow)" />
  <circle cx="888" cy="236" r="8" fill="#ffe88a" />
  <circle cx="922" cy="202" r="8" fill="#ffe88a" />
  <circle cx="964" cy="258" r="8" fill="#ffe88a" />
"""
    return wrap_svg("Song of the Rootbound", "Steam capsule concept art with giant lute silhouette and glowing musical roots", ["Song of the", "Rootbound"], defs, body)


def mist_and_marmalade() -> str:
    defs = common_defs("#ffcda7", "#6c8d97", "#ffbc7d")
    body = """
  <rect x="0" y="468" width="1232" height="238" fill="#684b3f" />
  <rect x="696" y="194" width="382" height="236" rx="26" fill="rgba(214,236,246,0.18)" stroke="rgba(255,255,255,0.28)" />
  <path d="M724 378 C798 310 864 312 942 262 C998 226 1046 224 1082 206" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="26" stroke-linecap="round" />
  <path d="M506 214 h228 c36 0 64 28 64 64 v58 c0 68 -52 120 -122 120 h-112 c-72 0 -122 -52 -122 -120 v-58 c0 -36 28 -64 64 -64 Z" fill="#ffbc7d" filter="url(#shadow)" />
  <path d="M780 260 h38 c30 0 52 22 52 52 v52" fill="none" stroke="#f5e5c5" stroke-width="18" stroke-linecap="round" />
  <path d="M572 202 C548 144 560 108 616 86 C598 150 642 154 662 90 C660 154 700 156 724 98" fill="none" stroke="rgba(255,255,255,0.86)" stroke-width="14" stroke-linecap="round" />
  <path d="M526 430 h194" stroke="#fff2dc" stroke-width="18" stroke-linecap="round" />
  <rect x="204" y="330" width="72" height="116" rx="18" fill="rgba(255,186,116,0.75)" />
  <rect x="296" y="308" width="80" height="138" rx="18" fill="rgba(255,220,142,0.75)" />
  <rect x="394" y="344" width="74" height="102" rx="18" fill="rgba(252,143,112,0.72)" />
  <circle cx="938" cy="466" r="28" fill="rgba(255,183,112,0.86)" />
  <circle cx="1008" cy="456" r="28" fill="rgba(136,210,240,0.86)" />
  <circle cx="1078" cy="470" r="28" fill="rgba(245,150,124,0.86)" />
  <rect x="922" y="490" width="32" height="68" rx="12" fill="#f2d0ae" />
  <rect x="992" y="480" width="32" height="78" rx="12" fill="#f2d0ae" />
  <rect x="1062" y="494" width="32" height="64" rx="12" fill="#f2d0ae" />
"""
    return wrap_svg("Mist & Marmalade", "Steam capsule concept art with oversized glowing teacup and weather-brewed steam", ["Mist &", "Marmalade"], defs, body)


def glassgarden_architects() -> str:
    defs = common_defs("#5cb8dd", "#113a59", "#ffd88c")
    body = """
  <path d="M0 0 L1232 0 L1232 132 C1078 154 934 220 804 346 C698 450 596 524 444 566 C308 604 170 600 0 584 Z" fill="rgba(255,255,255,0.08)" />
  <path d="M126 602 C216 532 334 500 466 500 C612 500 718 548 824 548 C958 548 1068 506 1176 426" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="18" stroke-linecap="round" />
  <path d="M116 624 C216 558 332 530 462 532 C596 534 722 578 844 580 C972 582 1084 548 1186 486" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="12" stroke-linecap="round" />
  <path d="M432 560 C432 434 532 338 656 338 C750 338 822 390 868 474 V560 Z" fill="rgba(255,255,255,0.16)" stroke="rgba(255,255,255,0.42)" stroke-width="8" />
  <path d="M688 574 C688 468 776 388 882 388 C964 388 1028 430 1068 494 V574 Z" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.38)" stroke-width="8" />
  <path d="M1014 52 C960 252 878 374 782 510" fill="none" stroke="rgba(255,242,174,0.76)" stroke-width="20" stroke-linecap="round" filter="url(#glow)" />
  <path d="M1068 34 C1012 230 934 354 846 476" fill="none" stroke="rgba(255,232,160,0.48)" stroke-width="12" stroke-linecap="round" />
  <circle cx="782" cy="510" r="22" fill="#ffd88c" filter="url(#glow)" />
  <path d="M584 560 C602 510 618 470 650 438" fill="none" stroke="#98f5d6" stroke-width="10" stroke-linecap="round" />
  <path d="M910 586 C926 536 944 496 970 464" fill="none" stroke="#98f5d6" stroke-width="10" stroke-linecap="round" />
  <circle cx="342" cy="246" r="14" fill="rgba(255,255,255,0.52)" />
  <circle cx="410" cy="216" r="10" fill="rgba(255,255,255,0.52)" />
  <circle cx="1044" cy="290" r="12" fill="rgba(255,255,255,0.52)" />
"""
    return wrap_svg("Glassgarden Architects", "Steam capsule concept art with prismatic underwater domes and dramatic sunbeams", ["Glassgarden", "Architects"], defs, body)


def the_kindness_audit() -> str:
    defs = common_defs("#f5c7a4", "#5e7b86", "#ffd09d")
    body = """
  <rect x="0" y="474" width="1232" height="232" fill="#745344" />
  <rect x="652" y="168" width="268" height="344" rx="24" fill="#f5eee0" transform="rotate(8 652 168)" filter="url(#shadow)" />
  <path d="M736 228 h98 M718 278 h126 M706 330 h142 M700 384 h132" stroke="#d6c9b6" stroke-width="14" stroke-linecap="round" />
  <circle cx="866" cy="438" r="84" fill="#ffcf9a" />
  <circle cx="866" cy="438" r="42" fill="#f58872" />
  <path d="M866 404 C886 368 930 360 960 386 C992 414 992 468 952 490 C922 506 890 494 866 468 C842 494 810 506 780 490 C740 468 740 414 772 386 C802 360 846 368 866 404 Z" fill="#f58872" filter="url(#glow)" />
  <rect x="298" y="194" width="176" height="242" rx="26" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.34)" />
  <rect x="214" y="464" width="820" height="26" rx="13" fill="#634738" />
  <rect x="208" y="490" width="842" height="146" rx="22" fill="#6d4f3f" />
  <rect x="780" y="520" width="84" height="84" rx="18" fill="#ffcb9f" />
  <rect x="878" y="500" width="92" height="104" rx="18" fill="#96d7c6" />
  <rect x="984" y="536" width="80" height="68" rx="18" fill="#f7a37c" />
  <path d="M786 624 C850 574 926 564 1016 568" fill="none" stroke="rgba(255,237,194,0.56)" stroke-width="10" stroke-linecap="round" />
"""
    return wrap_svg("The Kindness Audit", "Steam capsule concept art with giant heart stamp, papers, and civic desk glow", ["The Kindness", "Audit"], defs, body)


def driftwood_rails() -> str:
    defs = common_defs("#ffc89b", "#4b7194", "#ffe4a8")
    body = """
  <circle cx="1036" cy="116" r="78" fill="#ffe2b1" opacity="0.5" />
  <path d="M0 392 C146 362 312 404 484 376 C658 348 840 406 1020 380 C1104 368 1174 364 1232 356 V706 H0 Z" fill="#709abe" />
  <path d="M0 486 C164 462 330 508 500 484 C674 460 864 514 1028 492 C1110 480 1178 478 1232 472 V706 H0 Z" fill="#8ec0d6" />
  <path d="M0 566 C172 548 340 592 522 572 C708 552 874 602 1034 580 C1110 570 1176 568 1232 562 V706 H0 Z" fill="#f0cf9f" />
  <path d="M118 646 C244 576 360 540 496 510 C632 480 734 454 832 398 C908 354 980 300 1084 230" fill="none" stroke="#6d5344" stroke-width="24" stroke-linecap="round" />
  <path d="M122 646 C248 576 364 540 500 510 C636 480 738 454 836 398 C912 354 984 300 1088 230" fill="none" stroke="#b08668" stroke-width="8" stroke-linecap="round" />
  <path d="M172 620 L164 670 M270 586 L262 636 M368 556 L360 606 M468 526 L460 578 M566 496 L560 546 M664 462 L658 514 M758 426 L752 474 M850 376 L844 426 M944 322 L938 372" stroke="#4b392f" stroke-width="10" stroke-linecap="round" />
  <rect x="434" y="512" width="118" height="48" rx="18" fill="#a2704e" filter="url(#shadow)" />
  <circle cx="460" cy="566" r="18" fill="#453830" />
  <circle cx="528" cy="566" r="18" fill="#453830" />
  <rect x="456" y="470" width="64" height="38" rx="14" fill="#d4b183" />
  <path d="M960 310 C1006 286 1048 286 1096 304" fill="none" stroke="#fff1c7" stroke-width="10" stroke-linecap="round" />
  <circle cx="1076" cy="300" r="10" fill="#fff1c7" filter="url(#glow)" />
  <circle cx="1112" cy="324" r="10" fill="#fff1c7" filter="url(#glow)" />
  <circle cx="1148" cy="296" r="10" fill="#fff1c7" filter="url(#glow)" />
"""
    return wrap_svg("Driftwood Rails", "Steam capsule concept art with dynamic track diagonal and handcar heading to festival lights", ["Driftwood", "Rails"], defs, body)


def comet_croft() -> str:
    defs = common_defs("#6783d6", "#1f3760", "#ffe59a")
    body = """
  <path d="M0 0 C322 46 846 18 1232 0 V706 H0 Z" fill="rgba(255,255,255,0.05)" />
  <path d="M706 104 C770 50 858 30 962 26 C1056 22 1134 4 1216 -36" fill="none" stroke="rgba(255,255,255,0.24)" stroke-width="6" stroke-linecap="round" />
  <path d="M760 468 C782 372 864 320 964 320 H1120 C1210 320 1280 372 1298 468 L1308 560 H738 Z" fill="#6c593a" transform="translate(-120,0)" />
  <path d="M786 444 C822 384 886 350 970 350 H1114 C1198 350 1260 388 1290 444 L1300 504 H774 Z" fill="#8cc56a" transform="translate(-120,0)" />
  <path d="M834 374 v112 M914 370 v116 M994 370 v118 M1076 372 v116 M1158 380 v108" stroke="rgba(62,107,55,0.76)" stroke-width="8" transform="translate(-120,0)" />
  <path d="M834 424 C858 396 892 388 914 414 C936 440 974 440 994 414 C1016 388 1048 384 1076 414 C1100 440 1134 438 1158 410" fill="none" stroke="#d7f4a6" stroke-width="10" stroke-linecap="round" transform="translate(-120,0)" />
  <path d="M1080 96 C984 166 918 216 844 312" fill="none" stroke="#ffe59a" stroke-width="20" stroke-linecap="round" filter="url(#glow)" />
  <path d="M1128 70 C1030 148 958 198 884 290" fill="none" stroke="rgba(255,229,154,0.48)" stroke-width="10" stroke-linecap="round" />
  <path d="M1084 98 l74 -26 l-54 62" fill="#ffe59a" />
  <path d="M1146 56 l64 -22 l-46 56" fill="#ffe59a" />
  <circle cx="932" cy="558" r="28" fill="rgba(0,0,0,0.18)" />
"""
    return wrap_svg("Comet Croft", "Steam capsule concept art with bright comet diagonal and floating farmhouse island", ["Comet", "Croft"], defs, body)


SCENES = {
    "loom_and_lantern.svg": loom_and_lantern,
    "starlight_apiary.svg": starlight_apiary,
    "tide_painter.svg": tide_painter,
    "clockmakers_conservatory.svg": clockmakers_conservatory,
    "song_of_the_rootbound.svg": song_of_the_rootbound,
    "mist_and_marmalade.svg": mist_and_marmalade,
    "glassgarden_architects.svg": glassgarden_architects,
    "the_kindness_audit.svg": the_kindness_audit,
    "driftwood_rails.svg": driftwood_rails,
    "comet_croft.svg": comet_croft,
}


def main() -> None:
    asset_dir = Path(__file__).resolve().parent / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)

    for filename, build in SCENES.items():
        (asset_dir / filename).write_text(build(), encoding="utf-8")


if __name__ == "__main__":
    main()
