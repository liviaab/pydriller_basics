class CustomCommit:
    def __init__(self, index=None, pydrillerCommitObj=None, custom_obj=None):
        obj = {}
        if pydrillerCommitObj != None:
            obj = {
                "commit_index": index,
                "author_email": pydrillerCommitObj.author.email,
                "author_name": pydrillerCommitObj.author.name,
                "date": pydrillerCommitObj.author_date,
                "commit_hash": pydrillerCommitObj.hash,
                "files_changed": len(pydrillerCommitObj.modifications),
                "commit_message": pydrillerCommitObj.msg
            }

        if custom_obj != None:
            obj.update(custom_obj)

        self.commit = obj
        return

    def setCommit(self, index, pydrillerCommitObj, custom_obj=None):
        if pydrillerCommitObj != None:
            obj = {
                "commit_index": index,
                "author_email": pydrillerCommitObj.author.email,
                "author_name": pydrillerCommitObj.author.name,
                "date": pydrillerCommitObj.author_date,
                "commit_hash": pydrillerCommitObj.hash,
                "files_changed": len(pydrillerCommitObj.modifications),
                "commit_message": pydrillerCommitObj.msg
            }

        if custom_obj != None:
            obj.update(custom_obj)

        self.commit = obj
        return
    
    @classmethod
    def get_total_count_authors(cls, customCommitList):
        author_names = set()
        author_emails = set()
        for el in customCommitList:
            author_names.add(el["author_name"])
            author_emails.add(el["author_email"])
        
        return len(author_names), len(author_emails)
    
    @classmethod
    def get_migration_authors_count_between(cls, customCommitList, initialIndex, finalIndex):
        sortedList = sorted(customCommitList, key=lambda x: x["commit_index"])
        author_names = set()
        author_emails = set()

        for i in range(initialIndex, finalIndex+1):
            if sortedList[i]["are_we_interested"]:
                author_names.add(sortedList[i]["author_name"])
                author_emails.add(sortedList[i]["author_email"])

        return len(author_names), len(author_emails)

    @classmethod
    def characterize_authors(cls, customCommitList, initialIndex=None, finalIndex=None):
        sortedList = sorted(customCommitList, key=lambda x: x["commit_index"])
        authors = {}
        migration_authors = {}

        for i in range(len(sortedList)):
            commit = sortedList[i]
            email = commit["author_email"]

            if email in authors:
                authors[email] += 1
            else:
                authors[email] = 1

            # is the commit between the migration range and is it a migration commit?
            if (initialIndex != None and finalIndex != None) and \
                (i >= initialIndex and i <= finalIndex) and sortedList[i]["are_we_interested"]:
                if email in migration_authors:
                    migration_authors[email] += 1
                else:
                    migration_authors[email] = 1


        result = []
        for key, value in authors.items():
            result.append({
                "email": key,
                "total_commits": value,
                "migration_contributor": key in migration_authors,
                "migration_commits": migration_authors[key] if key in migration_authors else 0
            })

        return result
