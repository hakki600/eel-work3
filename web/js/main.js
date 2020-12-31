var search_btn = document.getElementById('search-btn');
var export_btn = document.getElementById('export-btn');
var result_area = document.getElementById('result-area');

async function search() {
    let result = await eel.search_kimetsu(input)();
    return result;
}

// 検索
search_btn.addEventListener('click', () => {
    // ユーザー入力文字
    input = document.searchform.character.value;
    if (!input) {
        window.alert("入力してください");
    }
    else {
        // pythonから検索関数を呼ぶ
        promise = search(input);
        promise.then((ret) => {
            result_area.value += ret + "\n";
        });
    }
})

// csv出力
export_btn.addEventListener('click', () => {
    // ユーザー入力文字
    filename = document.exportform.csvfilename.value;

    //正規表現パターン
    var regex = new RegExp(/.csv$/);

    //判定
    if (regex.test(filename)) {
        // pythonから出力関数を呼ぶ
        eel.export_kimetsu(filename);
        alert("エクスポートしました.");
    } else {
        alert("csvファイル名を入力してください. 「xxxxxx.csv」");
    }
})