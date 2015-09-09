<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <head>
    <title>69. Webアプリケーションの作成</title>
  </head>

  <body>
    <h1>ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．</h1><hr>

    <form action='/do_process' method='GET'>
      name: <input type='text' size=30 name='name' placeholder='Name' ><p>
      aliases_name: <input type='text' size=30 name='aliases_name' placeholder='Aliases_name'><p>
      tag: <input type='text' size=30 name='tag' placeholder='Tag'><p>
      <input type='submit' value='submit' name='button1'><p>
    </form>
  </body>
</html>
