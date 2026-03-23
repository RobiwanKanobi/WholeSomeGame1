from html import escape
from pathlib import Path


WIDTH = 1600
HEIGHT = 900


def wrap_svg(title: str, subtitle: str, defs: str, body: str) -> str:
    safe_title = escape(title)
    safe_subtitle = escape(subtitle)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title>{safe_title}</title>
  <desc>{safe_subtitle}</desc>
  <defs>
{defs}
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="36" fill="url(#bg)" />
  <rect x="28" y="28" width="{WIDTH - 56}" height="{HEIGHT - 56}" rx="30" fill="none" stroke="rgba(255,255,255,0.28)" />
  <rect x="80" y="76" width="460" height="120" rx="24" fill="rgba(255,251,247,0.14)" stroke="rgba(255,255,255,0.3)" />
  <text x="112" y="132" font-family="Inter, Arial, sans-serif" font-size="46" font-weight="700" fill="#fffaf6">{safe_title}</text>
  <text x="112" y="172" font-family="Inter, Arial, sans-serif" font-size="22" fill="rgba(255,250,246,0.82)">{safe_subtitle}</text>
{body}
</svg>
"""


def common_defs(start: str, end: str) -> str:
    return f"""    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{start}" />
      <stop offset="100%" stop-color="{end}" />
    </linearGradient>
    <linearGradient id="sunbeam" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="rgba(255,255,255,0.65)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="rgba(255,255,255,0.45)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0.08)" />
    </linearGradient>
    <linearGradient id="warm" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffd7ac" />
      <stop offset="100%" stop-color="#ff9e64" />
    </linearGradient>
    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
"""


def loom_and_lantern() -> str:
    defs = common_defs("#2d2d6d", "#f6b386")
    body = """
  <circle cx="1315" cy="170" r="82" fill="#ffd69e" opacity="0.42" />
  <path d="M0 520 C190 470 340 520 530 470 C720 420 880 500 1090 445 C1270 397 1415 470 1600 420 V900 H0 Z" fill="#2a3b68" />
  <path d="M0 600 C180 555 315 610 520 560 C720 510 910 585 1105 536 C1290 490 1430 565 1600 520 V900 H0 Z" fill="#3d4f87" />
  <path d="M0 690 C185 650 330 710 505 670 C700 620 930 720 1100 678 C1315 630 1465 700 1600 665 V900 H0 Z" fill="#4f3a57" />
  <rect x="940" y="230" width="16" height="430" rx="8" fill="#4b2f45" />
  <rect x="1160" y="230" width="16" height="430" rx="8" fill="#4b2f45" />
  <path d="M932 235 C970 165 1126 165 1168 235" fill="none" stroke="#5d3951" stroke-width="18" stroke-linecap="round" />
  <rect x="988" y="282" width="140" height="18" rx="9" fill="#5d3951" />
  <rect x="1024" y="318" width="9" height="284" fill="#f77f51" />
  <rect x="1053" y="318" width="9" height="284" fill="#ffd36f" />
  <rect x="1082" y="318" width="9" height="284" fill="#8fe0d7" />
  <rect x="1111" y="318" width="9" height="284" fill="#f7b4d1" />
  <path d="M1060 360 C1255 364 1320 520 1452 566" fill="none" stroke="#ffd48a" stroke-width="10" opacity="0.76" />
  <path d="M1115 392 C1290 420 1372 520 1508 598" fill="none" stroke="#8fe0d7" stroke-width="10" opacity="0.7" />
  <path d="M980 680 L1165 680 L1238 734 L850 734 Z" fill="#7a5e53" />
  <path d="M886 690 C1000 624 1118 624 1238 690" fill="none" stroke="#dbb58c" stroke-width="16" stroke-linecap="round" />
  <circle cx="908" cy="640" r="18" fill="#ffd493" filter="url(#softGlow)" />
  <circle cx="1208" cy="640" r="18" fill="#ffd493" filter="url(#softGlow)" />
  <rect x="166" y="670" width="72" height="84" rx="12" fill="#6d4f4f" />
  <rect x="250" y="628" width="92" height="126" rx="12" fill="#7d5960" />
  <rect x="360" y="660" width="108" height="94" rx="12" fill="#92686b" />
  <rect x="488" y="610" width="88" height="144" rx="12" fill="#7d5960" />
  <rect x="610" y="645" width="132" height="109" rx="12" fill="#6d4f4f" />
  <polygon points="154,670 203,628 252,670" fill="#4a3852" />
  <polygon points="238,628 296,572 354,628" fill="#533e58" />
  <polygon points="350,660 414,612 478,660" fill="#58405f" />
  <polygon points="474,610 532,558 590,610" fill="#533e58" />
  <polygon points="598,645 676,585 754,645" fill="#4a3852" />
  <circle cx="285" cy="640" r="10" fill="#ffd493" filter="url(#softGlow)" />
  <circle cx="534" cy="655" r="10" fill="#ffd493" filter="url(#softGlow)" />
  <circle cx="675" cy="676" r="10" fill="#ffd493" filter="url(#softGlow)" />
  <path d="M182 790 C420 750 660 760 855 796" stroke="rgba(255,225,180,0.48)" stroke-width="12" fill="none" stroke-linecap="round" />
  <circle cx="1310" cy="725" r="145" fill="rgba(255,212,138,0.12)" />
"""
    return wrap_svg("Loom & Lantern", "Textile village restoration at lantern-lit dusk", defs, body)


def starlight_apiary() -> str:
    defs = common_defs("#102044", "#1f4f73")
    body = """
  <circle cx="1315" cy="170" r="88" fill="#f8ecbc" opacity="0.56" />
  <path d="M0 625 C212 565 365 660 565 612 C748 566 925 640 1125 610 C1320 579 1482 640 1600 600 V900 H0 Z" fill="#10253f" />
  <path d="M0 720 C220 680 362 754 558 710 C780 660 940 752 1128 710 C1340 662 1495 726 1600 700 V900 H0 Z" fill="#163151" />
  <circle cx="980" cy="288" r="12" fill="#92e8ff" />
  <circle cx="1038" cy="246" r="9" fill="#92e8ff" />
  <circle cx="1088" cy="308" r="11" fill="#92e8ff" />
  <circle cx="1142" cy="262" r="9" fill="#92e8ff" />
  <circle cx="1186" cy="322" r="10" fill="#92e8ff" />
  <circle cx="1246" cy="272" r="8" fill="#92e8ff" />
  <path d="M980 288 L1038 246 L1088 308 L1142 262 L1186 322 L1246 272" fill="none" stroke="rgba(146,232,255,0.6)" stroke-width="4" />
  <rect x="290" y="330" width="190" height="240" rx="44" fill="url(#glass)" stroke="rgba(255,255,255,0.35)" />
  <rect x="340" y="370" width="92" height="150" rx="24" fill="rgba(255,210,124,0.28)" stroke="rgba(255,243,214,0.36)" />
  <path d="M536 380 h140 l32 42 v138 l-32 38 h-140 l-32 -38 v-138 z" fill="rgba(255,228,168,0.14)" stroke="rgba(255,255,255,0.34)" />
  <path d="M520 432 h168" stroke="rgba(255,255,255,0.2)" stroke-width="12" stroke-linecap="round" />
  <path d="M520 486 h168" stroke="rgba(255,255,255,0.2)" stroke-width="12" stroke-linecap="round" />
  <path d="M520 540 h168" stroke="rgba(255,255,255,0.2)" stroke-width="12" stroke-linecap="round" />
  <rect x="1010" y="485" width="192" height="174" rx="36" fill="rgba(255,255,255,0.16)" stroke="rgba(255,255,255,0.32)" />
  <path d="M1060 470 h92 v40 c0 30 -18 44 -46 44 c-28 0 -46 -14 -46 -44 z" fill="rgba(255,217,136,0.75)" stroke="rgba(255,255,255,0.28)" />
  <rect x="1088" y="446" width="36" height="30" rx="12" fill="rgba(255,231,190,0.86)" />
  <circle cx="1098" cy="596" r="18" fill="#7cf0ff" filter="url(#softGlow)" />
  <circle cx="1160" cy="560" r="14" fill="#7cf0ff" filter="url(#softGlow)" />
  <circle cx="1218" cy="608" r="17" fill="#7cf0ff" filter="url(#softGlow)" />
  <ellipse cx="922" cy="642" rx="24" ry="13" fill="#87ecff" opacity="0.86" />
  <ellipse cx="922" cy="642" rx="42" ry="10" fill="#87ecff" opacity="0.26" />
  <ellipse cx="1008" cy="602" rx="20" ry="11" fill="#87ecff" opacity="0.82" />
  <ellipse cx="1008" cy="602" rx="36" ry="9" fill="#87ecff" opacity="0.24" />
  <ellipse cx="970" cy="548" rx="18" ry="10" fill="#87ecff" opacity="0.8" />
  <ellipse cx="970" cy="548" rx="34" ry="8" fill="#87ecff" opacity="0.26" />
  <circle cx="232" cy="742" r="22" fill="#274f57" />
  <circle cx="294" cy="718" r="24" fill="#356d68" />
  <circle cx="352" cy="746" r="18" fill="#2f6156" />
  <circle cx="412" cy="722" r="24" fill="#2d575e" />
  <path d="M170 784 C338 716 470 732 590 786" stroke="#4ec8a3" stroke-width="10" fill="none" stroke-linecap="round" />
  <path d="M220 806 C370 750 502 764 628 804" stroke="#f8a6c7" stroke-width="10" fill="none" stroke-linecap="round" />
"""
    return wrap_svg("Starlight Apiary", "Glowing memory honey in a dreamlike night garden", defs, body)


def tide_painter() -> str:
    defs = common_defs("#ffd6b1", "#4ba3d7")
    body = """
  <circle cx="1290" cy="170" r="92" fill="#fff0c8" opacity="0.7" />
  <path d="M0 475 C196 430 358 470 548 442 C756 408 920 480 1134 450 C1310 424 1452 470 1600 446 V900 H0 Z" fill="#6ec3e8" />
  <path d="M0 566 C200 540 352 602 554 576 C764 548 934 620 1140 592 C1320 568 1460 606 1600 585 V900 H0 Z" fill="#3d91c7" />
  <path d="M0 676 C210 660 362 706 570 690 C796 672 954 730 1156 712 C1348 694 1480 728 1600 712 V900 H0 Z" fill="#f0c99f" />
  <path d="M0 742 C212 720 370 784 582 762 C784 740 980 798 1168 774 C1376 748 1488 786 1600 768 V900 H0 Z" fill="#efdcb4" />
  <path d="M866 650 C948 604 1048 604 1166 656" fill="none" stroke="#ff8765" stroke-width="16" stroke-linecap="round" />
  <path d="M880 694 C970 646 1062 648 1188 706" fill="none" stroke="#9dffde" stroke-width="14" stroke-linecap="round" />
  <path d="M1045 430 C1162 438 1266 502 1345 578" fill="none" stroke="rgba(255,255,255,0.62)" stroke-width="12" stroke-linecap="round" />
  <path d="M1088 468 C1202 470 1296 530 1368 612" fill="none" stroke="rgba(255,255,255,0.44)" stroke-width="9" stroke-linecap="round" />
  <rect x="392" y="560" width="16" height="168" rx="8" fill="#6a5348" transform="rotate(-18 392 560)" />
  <path d="M288 694 C352 634 416 604 484 604 C524 604 540 654 502 684 C438 734 374 748 306 734 Z" fill="#224f59" />
  <circle cx="554" cy="722" r="18" fill="#f8ad7f" />
  <circle cx="610" cy="698" r="22" fill="#f8ad7f" />
  <circle cx="662" cy="734" r="18" fill="#f8ad7f" />
  <path d="M508 734 C560 694 614 676 674 694" fill="none" stroke="rgba(255,255,255,0.34)" stroke-width="6" />
  <circle cx="482" cy="786" r="10" fill="#d28b66" />
  <circle cx="524" cy="816" r="9" fill="#d28b66" />
  <circle cx="576" cy="790" r="8" fill="#d28b66" />
  <circle cx="1180" cy="548" r="18" fill="rgba(255,255,255,0.4)" />
"""
    return wrap_svg("The Tide Painter", "Sunrise brushwork that guides a living shoreline", defs, body)


def clockmakers_conservatory() -> str:
    defs = common_defs("#9ad0ac", "#34555a")
    body = """
  <path d="M0 660 C220 598 392 686 590 638 C782 588 940 676 1140 632 C1320 590 1482 650 1600 618 V900 H0 Z" fill="#264143" />
  <path d="M180 760 V270 C180 220 228 176 280 176 H1320 C1372 176 1420 220 1420 270 V760" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.3)" stroke-width="8" />
  <path d="M348 760 V300 C348 258 380 226 420 226 H1180 C1220 226 1252 258 1252 300 V760" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="6" />
  <path d="M800 176 V760" stroke="rgba(255,255,255,0.22)" stroke-width="6" />
  <path d="M560 176 V760" stroke="rgba(255,255,255,0.16)" stroke-width="4" />
  <path d="M1040 176 V760" stroke="rgba(255,255,255,0.16)" stroke-width="4" />
  <path d="M800 176 C800 176 760 308 720 448 C684 576 628 674 560 760" fill="url(#sunbeam)" />
  <path d="M844 176 C844 176 922 326 1024 470 C1102 582 1180 666 1250 760" fill="url(#sunbeam)" />
  <circle cx="944" cy="458" r="126" fill="rgba(132,204,141,0.16)" />
  <circle cx="944" cy="458" r="84" fill="rgba(255,214,126,0.14)" stroke="#d8b267" stroke-width="12" />
  <circle cx="944" cy="458" r="24" fill="#d8b267" />
  <circle cx="944" cy="392" r="18" fill="#d8b267" />
  <circle cx="1002" cy="426" r="18" fill="#d8b267" />
  <circle cx="1002" cy="492" r="18" fill="#d8b267" />
  <circle cx="944" cy="526" r="18" fill="#d8b267" />
  <circle cx="886" cy="492" r="18" fill="#d8b267" />
  <circle cx="886" cy="426" r="18" fill="#d8b267" />
  <rect x="1036" y="294" width="16" height="324" rx="8" fill="#cbb088" />
  <circle cx="1044" cy="632" r="44" fill="#d6bb92" />
  <circle cx="1044" cy="632" r="16" fill="#6a5d54" />
  <path d="M454 760 C474 670 508 594 568 524 C610 476 644 412 656 356" fill="none" stroke="#5e8d5c" stroke-width="22" stroke-linecap="round" />
  <path d="M620 544 C560 512 524 486 492 444" fill="none" stroke="#7ecf86" stroke-width="14" stroke-linecap="round" />
  <path d="M604 456 C648 430 692 400 740 346" fill="none" stroke="#7ecf86" stroke-width="14" stroke-linecap="round" />
  <path d="M708 760 C734 662 764 572 818 496" fill="none" stroke="#5e8d5c" stroke-width="20" stroke-linecap="round" />
  <circle cx="614" cy="542" r="24" fill="#f8d48c" />
  <circle cx="596" cy="448" r="20" fill="#f8d48c" />
  <circle cx="832" cy="494" r="24" fill="#f8d48c" />
  <rect x="1090" y="630" width="118" height="20" rx="10" fill="#7a6253" />
  <rect x="1140" y="578" width="20" height="92" rx="10" fill="#7a6253" />
"""
    return wrap_svg("Clockmaker's Conservatory", "Brass flowers and greenhouse puzzles tending time itself", defs, body)


def song_of_the_rootbound() -> str:
    defs = common_defs("#17355b", "#2d5d4a")
    body = """
  <path d="M0 572 C190 520 392 598 552 560 C756 514 926 612 1128 562 C1304 520 1462 586 1600 550 V900 H0 Z" fill="#18334b" />
  <path d="M0 684 C204 646 372 716 576 680 C786 642 962 726 1166 692 C1336 662 1486 716 1600 688 V900 H0 Z" fill="#1b413f" />
  <circle cx="1280" cy="168" r="84" fill="#dff0c0" opacity="0.42" />
  <ellipse cx="342" cy="484" rx="52" ry="210" fill="#20422f" />
  <ellipse cx="1212" cy="474" rx="58" ry="220" fill="#21412f" />
  <ellipse cx="478" cy="450" rx="44" ry="182" fill="#1f3c2f" />
  <ellipse cx="1088" cy="434" rx="46" ry="196" fill="#1f3c2f" />
  <rect x="736" y="492" width="22" height="210" rx="11" fill="#3b2e31" />
  <circle cx="748" cy="446" r="52" fill="#f1b38d" />
  <path d="M680 690 C724 624 764 592 844 580" fill="none" stroke="#6d5036" stroke-width="20" stroke-linecap="round" />
  <path d="M820 470 C850 520 872 580 878 644" fill="none" stroke="#f0d7a1" stroke-width="10" stroke-linecap="round" />
  <path d="M682 630 C794 598 928 586 1076 604" fill="none" stroke="rgba(141,255,196,0.62)" stroke-width="6" />
  <path d="M658 662 C792 630 930 620 1094 642" fill="none" stroke="rgba(141,255,196,0.62)" stroke-width="6" />
  <path d="M636 694 C800 664 954 658 1110 680" fill="none" stroke="rgba(141,255,196,0.62)" stroke-width="6" />
  <circle cx="862" cy="636" r="14" fill="#9dffd3" filter="url(#softGlow)" />
  <circle cx="932" cy="620" r="14" fill="#9dffd3" filter="url(#softGlow)" />
  <circle cx="1012" cy="648" r="14" fill="#9dffd3" filter="url(#softGlow)" />
  <path d="M320 900 C410 812 510 768 624 726 C710 694 804 680 940 662 C1048 648 1190 604 1282 528" fill="none" stroke="rgba(120,255,192,0.36)" stroke-width="14" stroke-linecap="round" />
  <path d="M392 900 C462 830 554 778 656 748 C748 720 848 710 946 694 C1060 676 1168 640 1270 570" fill="none" stroke="rgba(120,255,192,0.24)" stroke-width="10" stroke-linecap="round" />
  <circle cx="1018" cy="366" r="8" fill="#ffe37a" />
  <circle cx="1058" cy="330" r="8" fill="#ffe37a" />
  <circle cx="1098" cy="390" r="8" fill="#ffe37a" />
  <circle cx="1148" cy="344" r="8" fill="#ffe37a" />
"""
    return wrap_svg("Song of the Rootbound", "Paper-cut forest harmonies healing a fractured woodland", defs, body)


def mist_and_marmalade() -> str:
    defs = common_defs("#ffcfab", "#648b97")
    body = """
  <rect x="0" y="546" width="1600" height="354" fill="#5d4638" />
  <rect x="162" y="244" width="590" height="360" rx="32" fill="rgba(255,255,255,0.24)" stroke="rgba(255,255,255,0.36)" />
  <path d="M212 466 C310 404 420 416 514 372 C586 338 640 320 702 320" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="24" stroke-linecap="round" />
  <circle cx="998" cy="622" r="96" fill="#ffb58d" opacity="0.14" />
  <rect x="918" y="284" width="442" height="252" rx="28" fill="rgba(211,234,244,0.28)" stroke="rgba(255,255,255,0.32)" />
  <path d="M936 470 C1020 396 1102 414 1188 352 C1266 296 1330 318 1352 300" fill="none" stroke="rgba(255,255,255,0.34)" stroke-width="34" stroke-linecap="round" />
  <rect x="236" y="534" width="1028" height="32" rx="16" fill="#7b5f4c" />
  <rect x="226" y="566" width="1056" height="204" rx="24" fill="#6a4f41" />
  <rect x="294" y="404" width="74" height="128" rx="18" fill="rgba(255,177,108,0.72)" />
  <rect x="392" y="384" width="82" height="148" rx="18" fill="rgba(255,213,137,0.72)" />
  <rect x="496" y="422" width="78" height="110" rx="18" fill="rgba(255,137,104,0.72)" />
  <rect x="602" y="396" width="86" height="136" rx="18" fill="rgba(148,215,239,0.72)" />
  <rect x="930" y="582" width="192" height="74" rx="32" fill="#f6f0de" />
  <path d="M986 582 C962 536 970 516 1020 496 C1002 552 1040 548 1058 496 C1052 548 1082 550 1104 504" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="12" stroke-linecap="round" />
  <circle cx="1210" cy="488" r="34" fill="rgba(255,183,112,0.82)" />
  <circle cx="1292" cy="472" r="34" fill="rgba(132,205,239,0.82)" />
  <circle cx="1372" cy="490" r="34" fill="rgba(246,139,118,0.82)" />
  <rect x="1188" y="520" width="44" height="90" rx="14" fill="#f6d8b3" />
  <rect x="1270" y="504" width="44" height="106" rx="14" fill="#f6d8b3" />
  <rect x="1350" y="522" width="44" height="88" rx="14" fill="#f6d8b3" />
  <circle cx="1018" cy="620" r="16" fill="#ffb27b" filter="url(#softGlow)" />
"""
    return wrap_svg("Mist & Marmalade", "A mountain tearoom brewing comfort out of weather", defs, body)


def glassgarden_architects() -> str:
    defs = common_defs("#5cb6d9", "#0f3958")
    body = """
  <path d="M0 0 C420 80 1180 20 1600 0 V900 H0 Z" fill="rgba(255,255,255,0.06)" />
  <path d="M0 0 L1600 0 L1600 176 C1348 210 1186 270 1040 376 C900 476 760 544 550 596 C396 634 200 628 0 598 Z" fill="rgba(255,255,255,0.08)" />
  <path d="M230 760 C330 682 450 644 590 642 C710 640 816 682 940 682 C1088 682 1194 626 1366 536" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="18" />
  <path d="M210 760 C300 698 430 674 566 684 C720 694 850 744 972 742 C1140 740 1274 688 1388 622" fill="none" stroke="rgba(255,255,255,0.16)" stroke-width="12" />
  <path d="M286 724 C286 584 404 470 548 470 C650 470 726 520 772 596 V724 Z" fill="url(#glass)" stroke="rgba(255,255,255,0.42)" stroke-width="8" />
  <path d="M642 748 C642 622 748 520 876 520 C964 520 1032 558 1082 630 V748 Z" fill="url(#glass)" stroke="rgba(255,255,255,0.4)" stroke-width="8" />
  <path d="M974 734 C974 634 1064 554 1178 554 C1262 554 1326 596 1370 660 V734 Z" fill="url(#glass)" stroke="rgba(255,255,255,0.4)" stroke-width="8" />
  <path d="M1188 62 C1126 320 1038 454 930 622" fill="none" stroke="rgba(255,247,176,0.7)" stroke-width="18" stroke-linecap="round" />
  <path d="M1264 42 C1188 294 1108 442 1028 588" fill="none" stroke="rgba(255,226,146,0.44)" stroke-width="12" stroke-linecap="round" />
  <circle cx="930" cy="620" r="26" fill="#ffd486" filter="url(#softGlow)" />
  <path d="M806 760 C822 700 842 654 878 616" fill="none" stroke="#93f6d6" stroke-width="12" stroke-linecap="round" />
  <path d="M1096 780 C1114 720 1132 676 1162 640" fill="none" stroke="#93f6d6" stroke-width="12" stroke-linecap="round" />
  <ellipse cx="516" cy="370" rx="22" ry="10" fill="rgba(255,255,255,0.56)" />
  <ellipse cx="610" cy="330" rx="26" ry="12" fill="rgba(255,255,255,0.56)" />
  <ellipse cx="1256" cy="406" rx="22" ry="10" fill="rgba(255,255,255,0.56)" />
  <ellipse cx="1322" cy="446" rx="26" ry="12" fill="rgba(255,255,255,0.56)" />
  <circle cx="462" cy="760" r="22" fill="#4bd5b5" opacity="0.5" />
  <circle cx="566" cy="776" r="18" fill="#7ce8ff" opacity="0.5" />
  <circle cx="930" cy="804" r="20" fill="#a4ffcf" opacity="0.42" />
"""
    return wrap_svg("Glassgarden Architects", "Sunlit underwater domes grown from blown glass", defs, body)


def the_kindness_audit() -> str:
    defs = common_defs("#f5c29d", "#587a86")
    body = """
  <rect x="0" y="602" width="1600" height="298" fill="#805b48" />
  <rect x="174" y="228" width="468" height="276" rx="26" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.34)" />
  <rect x="910" y="204" width="492" height="328" rx="26" fill="rgba(235,245,250,0.26)" stroke="rgba(255,255,255,0.34)" />
  <path d="M940 500 C1032 434 1110 444 1180 386 C1248 334 1312 338 1374 304" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="28" stroke-linecap="round" />
  <rect x="212" y="496" width="1150" height="44" rx="20" fill="#6d4b3d" />
  <rect x="252" y="544" width="1090" height="236" rx="24" fill="#715142" />
  <rect x="302" y="334" width="112" height="132" rx="18" fill="#fff5e8" transform="rotate(-8 302 334)" />
  <rect x="430" y="316" width="122" height="148" rx="18" fill="#fff1e0" transform="rotate(6 430 316)" />
  <circle cx="680" cy="380" r="42" fill="#ffbf87" />
  <path d="M680 340 C700 304 744 296 776 322 C810 350 810 404 766 426 C734 444 700 430 680 402 C660 430 626 444 594 426 C550 404 550 350 584 322 C616 296 660 304 680 340 Z" fill="#f48b7a" />
  <circle cx="1160" cy="580" r="72" fill="rgba(255,203,156,0.18)" />
  <rect x="1050" y="612" width="88" height="88" rx="18" fill="#ffcb9f" />
  <rect x="1150" y="582" width="98" height="118" rx="18" fill="#96d7c6" />
  <rect x="1260" y="632" width="84" height="68" rx="18" fill="#f7a37c" />
  <path d="M950 740 C1048 674 1128 680 1212 632 C1276 596 1338 586 1394 586" fill="none" stroke="rgba(255,234,190,0.55)" stroke-width="10" stroke-linecap="round" />
  <circle cx="344" cy="566" r="16" fill="#ffcb9f" />
  <circle cx="398" cy="594" r="14" fill="#96d7c6" />
  <circle cx="452" cy="568" r="14" fill="#f7a37c" />
  <circle cx="508" cy="598" r="16" fill="#ffcb9f" />
"""
    return wrap_svg("The Kindness Audit", "Civic magic powered by empathy, paper trails, and public upgrades", defs, body)


def driftwood_rails() -> str:
    defs = common_defs("#ffc596", "#446d93")
    body = """
  <circle cx="1274" cy="176" r="96" fill="#ffe0b0" opacity="0.52" />
  <path d="M0 512 C188 470 400 522 572 490 C766 452 958 540 1168 500 C1330 470 1460 510 1600 492 V900 H0 Z" fill="#729dbe" />
  <path d="M0 610 C216 580 406 642 590 620 C790 596 982 666 1188 638 C1374 614 1484 648 1600 634 V900 H0 Z" fill="#8fc4d9" />
  <path d="M0 696 C188 672 422 728 620 710 C848 688 988 752 1214 730 C1388 714 1490 748 1600 738 V900 H0 Z" fill="#f3d1a4" />
  <path d="M240 818 C334 760 422 732 518 712 C622 690 752 670 852 640 C952 608 1048 562 1196 454" fill="none" stroke="#6e5546" stroke-width="22" stroke-linecap="round" />
  <path d="M250 818 C344 760 434 732 530 712 C634 690 762 670 862 640 C964 608 1060 562 1208 454" fill="none" stroke="#b1856a" stroke-width="8" stroke-linecap="round" />
  <path d="M306 794 L296 842 M396 758 L388 810 M486 730 L478 784 M584 702 L576 758 M688 676 L680 732 M792 648 L784 704 M894 616 L886 674 M996 572 L990 628 M1100 520 L1092 576" stroke="#4e382f" stroke-width="10" stroke-linecap="round" />
  <rect x="620" y="676" width="124" height="54" rx="18" fill="#9b694d" />
  <circle cx="648" cy="738" r="20" fill="#4a3b34" />
  <circle cx="724" cy="738" r="20" fill="#4a3b34" />
  <rect x="648" y="622" width="70" height="46" rx="16" fill="#d4b184" />
  <path d="M1120 532 C1164 512 1208 514 1258 530" fill="none" stroke="#ffefc5" stroke-width="10" stroke-linecap="round" />
  <circle cx="1238" cy="522" r="10" fill="#ffefc5" filter="url(#softGlow)" />
  <circle cx="1278" cy="548" r="10" fill="#ffefc5" filter="url(#softGlow)" />
  <circle cx="1318" cy="516" r="10" fill="#ffefc5" filter="url(#softGlow)" />
  <circle cx="1358" cy="548" r="10" fill="#ffefc5" filter="url(#softGlow)" />
  <path d="M1218 560 C1250 520 1296 486 1356 472" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="8" stroke-linecap="round" />
"""
    return wrap_svg("Driftwood Rails", "Sunset handcar routes built across tidal flats for festival season", defs, body)


def comet_croft() -> str:
    defs = common_defs("#6b88d9", "#1d3559")
    body = """
  <path d="M0 0 C382 58 1024 18 1600 0 V900 H0 Z" fill="rgba(255,255,255,0.06)" />
  <path d="M328 690 C356 566 470 498 610 498 H980 C1120 498 1228 566 1260 690 L1286 796 H304 Z" fill="#6c583a" />
  <path d="M356 654 C398 582 486 540 612 540 H976 C1092 540 1184 586 1232 654 L1252 728 H334 Z" fill="#8cc66b" />
  <path d="M520 564 v160 M644 556 v168 M768 552 v172 M892 556 v168 M1016 566 v158" stroke="rgba(65,110,58,0.75)" stroke-width="10" />
  <path d="M520 632 C560 596 612 588 644 620 C678 652 734 652 768 622 C800 594 850 590 892 624 C930 654 982 650 1016 618" fill="none" stroke="#d7f3a5" stroke-width="12" stroke-linecap="round" />
  <path d="M1130 540 l0 164" stroke="#d9c18f" stroke-width="12" />
  <path d="M1130 540 l-56 38 l56 38 l56 -38 z" fill="#d9c18f" />
  <path d="M830 488 C880 414 960 374 1062 368 C1176 362 1284 304 1394 176" fill="none" stroke="rgba(255,255,255,0.34)" stroke-width="10" stroke-linecap="round" />
  <path d="M1166 250 l74 -28 l-56 64" fill="#ffe8af" />
  <path d="M1286 182 l82 -32 l-62 72" fill="#ffe8af" />
  <path d="M1076 294 l66 -24 l-48 58" fill="#ffe8af" />
  <circle cx="1236" cy="220" r="18" fill="#ffe8af" opacity="0.6" />
  <circle cx="1368" cy="146" r="14" fill="#ffe8af" opacity="0.6" />
  <circle cx="1140" cy="270" r="12" fill="#ffe8af" opacity="0.6" />
  <ellipse cx="792" cy="812" rx="270" ry="48" fill="rgba(0,0,0,0.18)" />
"""
    return wrap_svg("Comet Croft", "Sky-island farming beneath drifting constellations", defs, body)


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
