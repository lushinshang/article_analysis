
      let allAnswersVisible = true;

      function toggleAnswer(id, buttonElement) {
         const content = document.getElementById(id);
         if (!content) return;
         const isShown = content.classList.contains('show');

         if (!isShown) {
            content.style.maxHeight = 'auto';
            const scrollHeight = content.scrollHeight + 40;
            content.style.maxHeight = '0';
            content.offsetHeight;

            content.style.maxHeight = scrollHeight + "px";
            content.style.opacity = "1";
            content.style.paddingTop = "20px";
            content.style.paddingBottom = "20px";
            if (buttonElement) buttonElement.textContent = "隱藏答案與解析";
            content.classList.add('show');
         } else {
            content.style.maxHeight = "0";
            content.style.opacity = "0";
            content.style.paddingTop = "0";
            content.style.paddingBottom = "0";
            if (buttonElement) buttonElement.textContent = "顯示答案與解析";
            content.classList.remove('show');
         }
      }

      function toggleAllAnswers() {
         const answerContents = document.querySelectorAll('.answer-content');
         allAnswersVisible = !allAnswersVisible;

         answerContents.forEach((content) => {
            if (allAnswersVisible) {
               if (!content.classList.contains('show')) {
                  toggleAnswer(content.id, null);
               }
            } else {
               if (content.classList.contains('show')) {
                  toggleAnswer(content.id, null);
               }
            }
         });
         const toggleAllButton = document.getElementById('toggle-all-answers');
         if (toggleAllButton) {
            toggleAllButton.textContent = allAnswersVisible ? "隱藏全部解析" : "顯示全部解析";
         }
      }



      let allAnswersHidden = false;

      function toggleAllAnswersVisibility() {
         const hideAllButton = document.getElementById('hide-all-answers');
         allAnswersHidden = !allAnswersHidden;

         if (allAnswersHidden) {
            // 隱藏所有答案 - 取消選取所有正確答案
            hideAllCorrectAnswers();
            hideAllButton.textContent = "顯示所有答案";
         } else {
            // 顯示所有答案 - 重新選取所有正確答案
            showAllCorrectAnswers();
            hideAllButton.textContent = "隱藏所有答案";
         }
      }

      function hideAllCorrectAnswers() {
         // 取消選取所有 radio 和 checkbox
         const allInputs = document.querySelectorAll('input[type="radio"]:checked, input[type="checkbox"]:checked');
         allInputs.forEach(input => {
            input.checked = false;
         });

         // 清空所有配對題的文本輸入框
         const matchingInputs = document.querySelectorAll('input[type="text"][id*="_ans"]');
         matchingInputs.forEach(input => {
            input.value = '';
         });

         // 添加隱藏答案的 CSS 類別，移除高亮背景
         document.body.classList.add('answers-hidden');
      }

      function showAllCorrectAnswers() {
         // 重新選取所有正確答案
         // 這裡我們需要根據原始的 HTML 結構來恢復正確答案
         restoreCorrectAnswers();

         // 移除隱藏答案的 CSS 類別，恢復高亮背景
         document.body.classList.remove('answers-hidden');
      }

      function restoreCorrectAnswers() {
         // 儲存所有原始正確答案的資料
         const correctAnswers = [
            // Question 250
            { name: 'q250', value: 'A' },
            // Question 252  
            { name: 'q252', values: ['A', 'C'] }, // 多選題
            // Question 253
            { name: 'q253', value: 'A' },
            // Question 254
            { name: 'q254', value: 'D' },
            // Question 255 - 填充題，混淆矩陣
            // Question 256
            { name: 'q256', value: 'B' },
            // Question 257 - 多選題，A、B、D都不是不受監督學習
            { name: 'q257', values: ['A', 'B', 'D'] },
            // Question 258
            { name: 'q258', value: 'C' },
            // Question 259
            { name: 'q259', value: 'C' },
            // Question 260
            { name: 'q260', value: 'C' },
            // Question 261
            { name: 'q261', value: 'C' },
            // Question 262 - 填充題，隱私權和安全性
            // Question 263 - 填充題，溫度
            // Question 264
            { name: 'q264', value: 'D' },
            // Question 265 - 填充題，內嵌
            // Question 266
            { name: 'q266', values: ['C', 'D'] }, // 多選題
            // Question 267
            { name: 'q267', value: 'B' },
            // Question 268 - 配對題，A-A, B-B, C-C, D-D
            // Question 2
            { name: 'q2', value: 'B' },
            // Question 4
            { name: 'q4', value: 'D' },
            // Question 5
            { name: 'q5', value: 'A' },
            // Question 7
            { name: 'q7', value: 'A' },
            // Question 14
            { name: 'q14', values: ['A', 'C'] }, // 多選題
            // Question 15
            { name: 'q15', value: 'D' },
            // Question 17
            { name: 'q17', value: 'B' },
            // Question 18
            { name: 'q18', value: 'C' },
            // Question 20
            { name: 'q20', value: 'D' },
            // Question 23
            { name: 'q23', value: 'C' },
            // Question 25
            { name: 'q25', value: 'C' },
            // Question 26
            { name: 'q26', value: 'B' },
            // Question 29
            { name: 'q29', value: 'C' },
            // Question 31
            { name: 'q31', value: 'C' },
            // Question 34
            { name: 'q34', value: 'B' },
            // Question 35
            { name: 'q35', value: 'D' },
            // Question 37
            { name: 'q37', value: 'C' },
            // Question 39
            { name: 'q39', values: ['A', 'B'] }, // 多選題
            // Question 40
            { name: 'q40', values: ['A', 'B'] }, // 多選題
            // Question 41
            { name: 'q41', value: 'B' },
            // Question 45
            { name: 'q45', value: 'B' },
            // Question 46
            { name: 'q46', value: 'C' },
            // Question 49
            { name: 'q49', value: 'A' },
            // Question 50
            { name: 'q50', value: 'D' },
            // Question 52
            { name: 'q52', values: ['A', 'C'] }, // 多選題
            // Question 53
            { name: 'q53', value: 'A' },
            // Question 54
            { name: 'q54', value: 'A' },
            // Question 56
            { name: 'q56', value: 'B' },
            // Question 59
            { name: 'q59', value: 'A' },
            // Question 61
            { name: 'q61', value: 'B' },
            // Question 63
            { name: 'q63', value: 'A' },
            // Question 68
            { name: 'q68', value: 'C' },
            // Question 69
            { name: 'q69', value: 'A' },
            // Question 70
            { name: 'q70', value: 'C' },
            // Question 71
            { name: 'q71', value: 'B' },
            // Question 72
            { name: 'q72', values: ['D', 'E', 'F'] }, // 多選題
            // Question 73
            { name: 'q73', value: 'D' },
            // Question 79
            { name: 'q79', values: ['A', 'D'] }, // 多選題
            // Question 81
            { name: 'q81', value: 'B' },
            // Question 85
            { name: 'q85', value: 'D' },
            // Question 87
            { name: 'q87', value: 'A' },
            // Question 88
            { name: 'q88', value: 'D' },
            // Question 90
            { name: 'q90', value: 'C' },
            // Question 91
            { name: 'q91', values: ['C', 'D'] }, // 多選題
            // Question 93
            { name: 'q93', value: 'D' },
            // Question 95
            { name: 'q95', value: 'C' },
            // Question 96
            { name: 'q96', value: 'D' },
            // Question 97
            { name: 'q97', value: 'D' },
            // Question 100
            { name: 'q100', value: 'A' },
            // Question 101
            { name: 'q101', value: 'C' },
            // Question 102
            { name: 'q102', value: 'D' },
            // Question 103
            { name: 'q103', values: ['C', 'D'] }, // 多選題
            // Question 104
            { name: 'q104', value: 'D' },
            // Question 107
            { name: 'q107', value: 'C' },
            // Question 110
            { name: 'q110', value: 'B' },
            // Question 111
            { name: 'q111', values: ['A', 'B', 'C'] }, // 多選題
            // Question 117
            { name: 'q117', value: 'D' },
            // Question 118
            { name: 'q118', value: 'C' },
            // Question 119
            { name: 'q119', value: 'B' },
            // Question 121
            { name: 'q121', value: 'B' },
            // Question 122
            { name: 'q122', value: 'B' },
            // Question 124
            { name: 'q124', values: ['A', 'D'] }, // 多選題
            // Question 127
            { name: 'q127', value: 'C' },
            // Question 128
            { name: 'q128', value: 'C' },
         ];

         correctAnswers.forEach(answer => {
            if (answer.values) {
               // 多選題 (checkbox)
               answer.values.forEach(value => {
                  const input = document.querySelector(`input[name="${answer.name}"][value="${value}"]`);
                  if (input) input.checked = true;
               });
            } else {
               // 單選題 (radio)
               const input = document.querySelector(`input[name="${answer.name}"][value="${answer.value}"]`);
               if (input) input.checked = true;
            }
         });

         // 恢復配對題答案
         const matchingAnswers = [
            // Question 1 (配對題)
            { id: 'q1_ans1', value: 'C' },
            { id: 'q1_ans2', value: 'B' },
            { id: 'q1_ans3', value: 'A' },
            // Question 6 (配對題)
            { id: 'q6_ans1', value: 'A' },
            { id: 'q6_ans2', value: 'B' },
            { id: 'q6_ans3', value: 'C' },
            // Question 19 (配對題)
            { id: 'q19_ans1', value: 'A' },
            { id: 'q19_ans2', value: 'B' },
            { id: 'q19_ans3', value: 'C' },
            // Question 22 (配對題)
            { id: 'q22_ans1', value: 'A' },
            { id: 'q22_ans2', value: 'B' },
            { id: 'q22_ans3', value: 'C' },
            // Question 38 (配對題)
            { id: 'q38_ans1', value: 'A' },
            { id: 'q38_ans2', value: 'B' },
            { id: 'q38_ans3', value: 'D' },
            // Question 43 (配對題)
            { id: 'q43_ans1', value: 'A' },
            { id: 'q43_ans2', value: 'B' },
            { id: 'q43_ans3', value: 'C' },
            // Question 48 (配對題)
            { id: 'q48_ans1', value: 'A' },
            { id: 'q48_ans2', value: 'C' },
            { id: 'q48_ans3', value: 'B' },
            // Question 55 (配對題)
            { id: 'q55_ans1', value: 'B' },
            { id: 'q55_ans2', value: 'C' },
            { id: 'q55_ans3', value: 'B' },
            // Question 62 (配對題)
            { id: 'q62_ans1', value: 'A' },
            { id: 'q62_ans2', value: 'B' },
            { id: 'q62_ans3', value: 'C' },
            // Question 67 (配對題)
            { id: 'q67_ans1', value: 'B' },
            { id: 'q67_ans2', value: 'C' },
            // Question 92 (配對題)
            { id: 'q92_ans1', value: 'A' },
            { id: 'q92_ans2', value: 'C' },
            { id: 'q92_ans3', value: 'B' },
            // Question 108 (配對題)
            { id: 'q108_ans1', value: 'A' },
            { id: 'q108_ans2', value: 'B' },
         ];

         matchingAnswers.forEach(answer => {
            const input = document.getElementById(answer.id);
            if (input) input.value = answer.value;
         });
      }

      function filterQuestions(category, clickedButton) {
         const questionCards = document.querySelectorAll('#questions-wrapper .question-card');
         const filterButtons = document.querySelectorAll('.outline-filter button');

         filterButtons.forEach(button => button.classList.remove('active'));
         if (clickedButton) clickedButton.classList.add('active');

         questionCards.forEach(card => {
            const cardCategories = card.dataset.category ? card.dataset.category.split(' ') : [];
            if (category === 'all' || cardCategories.includes(category)) {
               card.classList.remove('hidden');
            } else {
               card.classList.add('hidden');
            }
         });
      }

      function updateFilterCounts() {
         const questionCards = document.querySelectorAll('#questions-wrapper .question-card');
         const filterButtons = document.querySelectorAll('.outline-filter button');

         filterButtons.forEach(button => {
            const filter = button.dataset.filter;
            let count = 0;
            let baseText = "";

            const currentText = button.textContent;
            const parenIndex = currentText.lastIndexOf('(');
            if (parenIndex > 0 && currentText.endsWith(')')) {
               baseText = currentText.substring(0, parenIndex).trim();
            } else {
               baseText = currentText;
            }

            if (baseText === "" || !isNaN(parseInt(baseText.charAt(0)))) {
               switch (filter) {
                  case 'all': baseText = "全部顯示"; break;
                  case 'outline-1': baseText = "描述人工智慧工作負載和考量"; break;
                  case 'outline-2': baseText = "描述 Azure 上機器學習的基本原則"; break;
                  case 'outline-3': baseText = "描述 Azure 上的電腦視覺工作負載的特點"; break;
                  case 'outline-4': baseText = "描述 Azure 上自然語言處理 (NLP) 工作負載的特點"; break;
               }
            }

            if (filter === 'all') {
               count = questionCards.length;
            } else {
               questionCards.forEach(card => {
                  const cardCategories = card.dataset.category ? card.dataset.category.split(' ') : [];
                  if (cardCategories.includes(filter)) {
                     count++;
                  }
               });
            }
            button.textContent = `${baseText} (${count})`;
         });
      }

      // Function to store original titles before any modification
      function storeOriginalTitles() {
         const titleElements = document.querySelectorAll('.question-title');
         titleElements.forEach(titleEl => {
            if (!titleEl.dataset.originalTitle) { // Store only once
               titleEl.dataset.originalTitle = titleEl.textContent.trim();
            }
         });
      }

      // Fisher-Yates Shuffle Algorithm
      function shuffleArray(array) {
         for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
         }
      }

      // Renumber questions from #1, supporting both page structures:
      // - part1: question cards are direct children of .container (outside #questions-wrapper)
      // - part2: question cards are already inside #questions-wrapper
      function randomizeAndRenumberQuestions() {
         storeOriginalTitles();

         const questionsWrapper = document.getElementById('questions-wrapper');
         if (!questionsWrapper) return;

         // Try to get cards already inside the wrapper (part2 structure)
         let allQuestionCards = Array.from(questionsWrapper.querySelectorAll(':scope > .question-card'));

         // If wrapper is empty, fetch from .container direct children and move them in (part1 structure)
         if (allQuestionCards.length === 0) {
            const containerCards = Array.from(document.querySelectorAll('.container > .question-card'));
            containerCards.forEach(card => questionsWrapper.appendChild(card));
            allQuestionCards = Array.from(questionsWrapper.querySelectorAll(':scope > .question-card'));
         }

         if (allQuestionCards.length === 0) return;

         //shuffleArray(allQuestionCards); // 取消註解此行以啟用亂數排序

         // Renumber all question cards sequentially from #1
         allQuestionCards.forEach((card, index) => {
            const titleElement = card.querySelector('.question-title');
            if (titleElement) {
               // Use stored original title or current text content
               const originalTitleText = titleElement.dataset.originalTitle || titleElement.textContent.trim();
               if (!titleElement.dataset.originalTitle) {
                  titleElement.dataset.originalTitle = originalTitleText;
               }

               let typeDescription = "";

               // Extract question type from parentheses, e.g. "(配對題)", "(選擇題)"
               const match = originalTitleText.match(/\((.*?)\)/);
               if (match && match[1]) {
                  typeDescription = `(${match[1]})`;
               } else {
                  // No parentheses found and not a Chinese-numbered title — wrap whole text
                  if (!originalTitleText.startsWith("第") || !originalTitleText.includes("題")) {
                     typeDescription = `(${originalTitleText})`;
                  }
               }

               titleElement.textContent = `#${index + 1} ${typeDescription}`.trim();
            }
         });
      }


      document.addEventListener('DOMContentLoaded', () => {
         const answerContents = document.querySelectorAll('.answer-content');
         answerContents.forEach(content => {
            content.style.maxHeight = 'none';
            content.style.opacity = '1';
            content.style.paddingTop = '20px';
            content.style.paddingBottom = '20px';
            content.classList.add('show');
         });

         randomizeAndRenumberQuestions(); // Move cards into wrapper and renumber
         updateFilterCounts(); // Update filter counts based on questions now in wrapper

         const toggleAllButton = document.getElementById('toggle-all-answers');
         if (toggleAllButton) {
            toggleAllButton.addEventListener('click', toggleAllAnswers);
            toggleAllButton.textContent = "隱藏全部解析";
         }

         const hideAllButton = document.getElementById('hide-all-answers');
         if (hideAllButton) {
            hideAllButton.addEventListener('click', toggleAllAnswersVisibility);
         }

         const filterButtons = document.querySelectorAll('.outline-filter button');
         filterButtons.forEach(button => {
            if (!button.hasAttribute('onclick')) {
               button.addEventListener('click', () => filterQuestions(button.dataset.filter, button));
            }
         });
      });
   
