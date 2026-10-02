# Reproduce this demonstration

Use version 0.2.0 main.splash. Set OCTO_CARD_HOST to the Windows reference host and launch octocard.bat. Use a fresh application-data directory for a clean run; do not erase existing user files to reproduce a test.

1. Empty input: choose organize; expect an input prompt and no saved file.
2. Unrelated text: enter a walking note; expect no action.
3. Enter `邮件草稿：本周修复了统计界面，新增事项已验证。邮件还没写完。`; organize. Source remains in the editable draft, followed by a neutral closing.
4. Change the source and confirm save: expect a request to organize again, with no write.
5. Organize again, edit the draft and confirm: expect “已保存并核验，尚未发送”. Check application-isolated user-draft.txt equals the editor contents, and draft-state.json contains the matching source/draft.
6. Confirm again: file content stays identical. Close only this app, relaunch with the same data directory: expect restored draft.
7. Cancel and confirm: prior saved contents remain unchanged. Clear data: the two current draft files disappear.
8. Failure test only in a separate, disposable test-data directory: create an empty directory named user-draft.txt; organize and confirm. Expect an explicit save failure, without a success claim. Remove only this exact empty directory after closing the test app.
9. In a separate test directory, provide mismatching state and draft files; relaunch and confirm. Expect save blocked until new organization; existing file is unchanged.

Observed results: mail-mvp.json and demo-results.json. Synthetic examples only. These results do not establish competition acceptance.

Host executable SHA-256: BF277982100470A5C2AE0C9E5AEA556802ED7A61ADD64432D606BA2A79DAB1EF. Local App Hub source HEAD was 0f332112f0b5a379c5bb33790df74b21597190cf, with an existing modified Cargo.lock; exact binary build provenance remains unverified. Do not substitute that source ID for proof of an identical binary. A reproducible clean host build remains a delivery task.
