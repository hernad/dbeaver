package org.jkiss.dbeaver.ext.postgresql.tasks;

import org.jkiss.dbeaver.ext.postgresql.model.PostgreDatabase;
import org.jkiss.dbeaver.model.edit.DBEPersistAction;
import org.jkiss.dbeaver.model.exec.DBCException;
import org.jkiss.dbeaver.model.exec.DBCSession;
import org.jkiss.dbeaver.model.impl.edit.SQLDatabasePersistAction;
import org.jkiss.dbeaver.model.sql.task.SQLToolExecuteHandler;

import java.util.List;

public class PostgreToolDatabaseAnalyze extends SQLToolExecuteHandler<PostgreDatabase, PostgreToolDatabaseAnalyzeSettings> {

    @Override
    public PostgreToolDatabaseAnalyzeSettings createToolSettings() {
        return new PostgreToolDatabaseAnalyzeSettings();
    }

    @Override
    public void generateObjectQueries(DBCSession session, PostgreToolDatabaseAnalyzeSettings settings, List<DBEPersistAction> queries, PostgreDatabase object) throws DBCException {
        queries.add(new SQLDatabasePersistAction("ANALYZE VERBOSE"));
    }
}
