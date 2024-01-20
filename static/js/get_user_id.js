/* 関数getUserIDの中身の一部 */
export function getUserID() {
    //最初に、アクセスしてきたユーザが自分のuserIDを持っていることを確認する
    const userID = localStorage.getItem("user");

    //userIDを持っていない場合、新しくuserIDを付与する
    //ない場合は多分nullかundefinedになる

    if (!(userID == null || userID == undefined)) {
        //存在する場合、既存のuserIDを返す
        return userID;
    } else {
        //存在しない場合、新規userIDを作成してそれを返す

        //UUIDを取得
        let newUserID = self.crypto.randomUUID(); //ランダムに生成された36文字長のv4 UUIDを含む文字列

        //DBにデータを保存
        localStorage.setItem("user", newUserID);
        return newUserID;
    }
}
