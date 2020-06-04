package org.jkiss.dbeaver.ext.postgresql.tasks;

import org.jkiss.code.NotNull;
import org.jkiss.dbeaver.ext.postgresql.model.PostgreDatabase;
import org.jkiss.dbeaver.model.edit.DBEPersistAction;
import org.jkiss.dbeaver.model.exec.DBCException;
import org.jkiss.dbeaver.model.exec.DBCSession;
import org.jkiss.dbeaver.model.impl.edit.SQLDatabasePersistAction;
import org.jkiss.dbeaver.model.sql.task.SQLToolExecuteHandler;

import java.util.List;

public class PostgreToolDatabaseVacuum extends SQLToolExecuteHandler<PostgreDatabase, PostgreToolDatabaseVacuumSettings> {
    @NotNull
    @Override
    public PostgreToolDatabaseVacuumSettings createToolSettings() {
        return new PostgreToolDatabaseVacuumSettings();
    }

    @Override
    public void generateObjectQueries(DBCSession session, PostgreToolDatabaseVacuumSettings settings, List<DBEPersistAction> queries, PostgreDatabase object) throws DBCException {
        String sql = "VACUUM (";
        boolean isFull = settings.isFull();
        boolean isFreeze = settings.isFreeze();
        if(isFull) sql += "FULL, ";
        if(isFreeze) sql += "FREEZE, ";
        sql += "VERBOSE";
        boolean isAnalyzed = settings.isAnalyzed();
        boolean isDisabled = settings.isDisableSkipping();
        if(isAnalyzed) sql += ", ANALYZE";
        if(isDisabled) sql += ", DISABLE_PAGE_SKIPPING";
        sql += ")";
        queries.add(new SQLDatabasePersistAction(sql));
    }
}
