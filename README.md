# 알바췍 공식 홈페이지

https://bygjun.github.io/albacheck-official/

알바췍의 실제 앱 화면, 사용 가이드, 개인정보 처리방침, Google Play 설치 안내를 제공하는 정적 홈페이지입니다.

## 배포

GitHub Pages는 `main` 브랜치의 `/docs`를 게시합니다. `.nojekyll`로 정적 파일을 그대로 제공합니다. 사이트 변경 후 검수하고 main에 푸시하면 배포됩니다.

```sh
python3 scripts/validate_site.py
node --check docs/assets/site.js
```

## 검색과 설치

페이지별 제목·설명·canonical·OG, WebSite/SoftwareApplication/Article/FAQPage JSON-LD, 사이트맵을 제공합니다. 원문 내용과 구조화 데이터는 일치하도록 유지합니다. sitemap: https://bygjun.github.io/albacheck-official/sitemap.xml

GitHub Pages의 프로젝트 경로에서 제공되는 robots.txt는 도메인 루트 robots.txt 제어를 대신하지 않습니다. 색인/검색 노출/AI 인용은 별도로 관측해야 합니다.

설치 링크는 `com.albacheck`, `utm_source=website`, `utm_campaign=official_site`를 사용합니다. UTM만으로 실제 설치나 방문이 모두 측정된다고 보장하지 않습니다.

앱 화면은 실제 앱의 화면이며 금액·근무지는 예시입니다. 문의 문장은 자동 전송되지 않습니다. 계산 결과는 입력 조건에 따른 참고 값입니다.

## 에셋

실제 알바췍 앱 아이콘과 스크린샷, 기존 홍보용 독자적인 햄스터 일러스트를 사용합니다. 글꼴은 Pretendard입니다.

## 검색 도구 소유권

Google Search Console은 호스트 전체 URL 접두사 `https://bygjun.github.io/`와 루트 `https://bygjun.github.io/sitemap.xml`을 사용합니다. 호스트 인증·robots·루트 사이트맵은 [bygjun/bygjun.github.io](https://github.com/bygjun/bygjun.github.io)에서 관리합니다. 홈페이지의 Google 인증 태그를 보존하세요. 이 프로젝트의 기존 sitemap.xml은 네이버 등록과 호환을 위해 유지합니다. 두 XML의 실제 공식 페이지 URL 목록을 함께 유지하세요.

## Instagram 짧은 설치 주소

`https://bygjun.github.io/albacheck-official/ig/`는 Instagram 프로필에서 사용하는 설치 이동 주소입니다. 쿼리가 없는 자체 도메인 주소로 입력 길이와 percent 중복 인코딩 문제를 피합니다. 0초 meta refresh와 동일한 목적지의 수동 설치 버튼을 제공하며, 목적지는 `com.albacheck`의 Google Play로 고정합니다. `utm_source=ig`, `utm_medium=social`, `utm_campaign=albacheck_profile`, `utm_content=link_in_bio`를 top-level과 encoded Install Referrer에 함께 전달합니다. 다른 홈페이지 CTA의 website 출처는 유지합니다. 이동 페이지는 noindex이며 사이트맵에 추가하지 않습니다. 페이지 접근 또는 정상 이동은 실제 설치 완료나 귀속 성공을 뜻하지 않습니다.
