document.addEventListener('DOMContentLoaded', () => {
    const imageFiles = [
        'さるもきからおちる.png',
        '失敗は成功の母.png',
        '出る杭は打たれる.png',
        '情けは人の為ならず.png',
        '石橋を叩いて渡る.png',
        '二兎を追う者は一兎をも得ず.png',
        '馬の耳に念仏.png'
    ];

    const questionTextElement = document.getElementById('question-text');
    const imageElements = [
        document.getElementById('image1'),
        document.getElementById('image2'),
        document.getElementById('image3')
    ];
    const resultFeedbackElement = document.getElementById('result-feedback');
    const finishMessageElement = document.getElementById('finish-message');

    const imageSelectionArea = document.getElementById('image-selection-area');
    const resultDisplayArea = document.getElementById('result-display-area');


    let currentRound = 0;
    const totalRounds = 3;
    let correctAnswerFile = '';

    async function startGame() {
        currentRound = 0;
        finishMessageElement.classList.add('hidden');
        finishMessageElement.textContent = '';
        resultFeedbackElement.innerHTML = ''; // 前回の結果をクリア
        await nextRound();
    }

    async function nextRound() {
        if (currentRound >= totalRounds) {
            endGame();
            return;
        }

        clearForNextRound();

        // 画像フォルダの中の画像ファイルからランダムに3つを選ぶ
        const shuffledFiles = [...imageFiles].sort(() => 0.5 - Math.random());
        const selectedFiles = shuffledFiles.slice(0, 3);

        // 選んだ3つの画像ファイルの中から1つを選んで、それを答えとする
        correctAnswerFile = selectedFiles[Math.floor(Math.random() * selectedFiles.length)];

        // 答えの画像ファイルのファイル名から拡張子以外の部分を取り出して、それを問題文とする
        const question = correctAnswerFile.replace('.png', '');
        questionTextElement.textContent = question;

        // 問題文と選んだ3つの画像ファイルをウィンドウに表示する
        imageSelectionArea.classList.remove('hidden');
        selectedFiles.forEach((file, index) => {
            imageElements[index].src = `画像/${file}`;
            imageElements[index].dataset.fileName = file; // 答え合わせのためにファイル名を保持
            imageElements[index].classList.remove('hidden');
            imageElements[index].onclick = handleImageClick;
        });

        currentRound++;
    }

    async function handleImageClick(event) {
        // クリックイベントを一時的に無効化
        imageElements.forEach(img => img.onclick = null);

        const clickedImageFile = event.target.dataset.fileName;
        resultDisplayArea.classList.remove('hidden');
        resultFeedbackElement.innerHTML = ''; // 前回のフィードバックをクリア

        const feedbackDiv = document.createElement('div');
        if (clickedImageFile === correctAnswerFile) {
            feedbackDiv.classList.add('correct-answer-feedback');
        } else {
            feedbackDiv.classList.add('incorrect-answer-feedback');
        }
        resultFeedbackElement.appendChild(feedbackDiv);

        // 1秒待つ
        await new Promise(resolve => setTimeout(resolve, 1000));

        // ウィンドウをクリアして、繰り返しの始めに戻る
        await nextRound();
    }

    function clearForNextRound() {
        questionTextElement.textContent = '';
        imageElements.forEach(img => {
            img.src = '';
            img.classList.add('hidden'); // 画像を非表示に
            img.onclick = null;
            delete img.dataset.fileName;
        });
        resultFeedbackElement.innerHTML = '';
        resultDisplayArea.classList.add('hidden');
        finishMessageElement.classList.add('hidden');
    }

    function endGame() {
        clearForNextRound();
        imageSelectionArea.classList.add('hidden'); // 画像選択エリアも非表示
        questionTextElement.textContent = ''; // 問題文もクリア
        resultFeedbackElement.innerHTML = ''; // 結果表示もクリア

        finishMessageElement.textContent = 'F5キーをおすと、もういちどできます';
        finishMessageElement.classList.remove('hidden');
    }

    // ゲーム開始
    startGame();
});