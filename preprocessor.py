import os
import sys
import cPickle
import logging

def configure_tiler():
        tiler.defineBoundingBox(tiler_output_dir) # ***
        general_lyrs = tiler.processGeneralLayers() # ***
        ## Configure
        # Rollback Disturbances
        rollback_dist_lookup = {
            1: "Wild Fires",
            2: "Clearcut harvesting with salvage",
            13: "SlashBurning"
        }
        rollback_name_lookup = {
            1: "fire",
            2: "harvest",
            13: "slashburn"
        }
        tiler.processRollbackDisturbances(rollback_dist_lookup, rollback_name_lookup)

        # Historic Fire Disturbances
        fire_dt = "Wild Fires"
        tiler.processHistoricFireDisturbances(historicFire1, fire_dt)
        tiler.processHistoricFireDisturbances(historicFire2, fire_dt)

        # Historic Harvest
        cc_dt = "Clearcut harvesting with salvage"
        sb_dt = "SlashBurning"
        tiler.processHistoricHarvestDisturbances(historicHarvest, sb_base_percent, cc_dt, sb_dt)

        # Historic Insect
        if historicInsect.getWorkspace() != None:
            insect_attribute = "Severity"
            insect_attribute_dist_type_lookup = {
                "V": "Mountain Pine Beetle - Very Severe Impact",
                "S": "Mountain Pine Beetle - Severe Impact",
                "M": "Mountain Pine Beetle - Moderate Impact",
                "L": "Mountain Pine Beetle - Low Impact",
                "4": "Mountain Pine Beetle - Very Severe Impact",
                "3": "Mountain Pine Beetle - Severe Impact",
                "2": "Mountain Pine Beetle - Moderate Impact",
                "1": "Mountain Pine Beetle - Low Impact"
            }
            tiler.processHistoricInsectDisturbances(historicInsect, insect_attribute, insect_attribute_dist_type_lookup)
        return general_lyrs

def save_inputs():
    try:
        print "---------------------\nSaving inputs...",
        if not os.path.exists('inputs'):
            os.mkdir('inputs')
        cPickle.dump(inventory, open(r'inputs\inventory.pkl', 'wb'))
        cPickle.dump(historicFire1, open(r'inputs\historicFire1.pkl', 'wb'))
        cPickle.dump(historicFire2, open(r'inputs\historicFire2.pkl', 'wb'))
        cPickle.dump(historicHarvest, open(r'inputs\historicHarvest.pkl', 'wb'))
        cPickle.dump(historicInsect, open(r'inputs\historicInsect.pkl', 'wb'))
        cPickle.dump(rollbackDisturbances, open(r'inputs\rollbackDisturbances.pkl', 'wb'))
        cPickle.dump(spatialBoundaries, open(r'inputs\spatialBoundaries.pkl', 'wb'))
        cPickle.dump(NAmat, open(r'inputs\NAmat.pkl', 'wb'))
        cPickle.dump(transitionRules, open(r'inputs\transitionRules.pkl', 'wb'))
        cPickle.dump(yieldTable, open(r'inputs\yieldTable.pkl', 'wb'))
        cPickle.dump(AIDB, open(r'inputs\AIDB.pkl', 'wb'))
        cPickle.dump(resolution, open(r'inputs\resolution.pkl', 'wb'))
        cPickle.dump(rollback_enabled, open(r'inputs\rollback_enabled.pkl', 'wb'))
        cPickle.dump(historic_range, open(r'inputs\historic_range.pkl', 'wb'))
        cPickle.dump(rollback_range, open(r'inputs\rollback_range.pkl', 'wb'))
        cPickle.dump(future_range, open(r'inputs\future_range.pkl', 'wb'))
        cPickle.dump(activity_start_year, open(r'inputs\activity_start_year.pkl', 'wb'))
        cPickle.dump(inventory_raster_out, open(r'inputs\inventory_raster_out.pkl', 'wb'))
        cPickle.dump(tiler_scenarios, open(r'inputs\tiler_scenarios.pkl', 'wb'))
        cPickle.dump(GCBM_scenarios, open(r'inputs\GCBM_scenarios.pkl', 'wb'))
        cPickle.dump(tiler_output_dir, open(r'inputs\tiler_output_dir.pkl', 'wb'))
        cPickle.dump(recliner2gcbm_config_dir, open(r'inputs\recliner2gcbm_config_dir.pkl', 'wb'))
        cPickle.dump(recliner2gcbm_output_path, open(r'inputs\recliner2gcbm_output_path.pkl', 'wb'))
        cPickle.dump(recliner2gcbm_exe_path, open(r'inputs\recliner2gcbm_exe_path.pkl', 'wb'))
        cPickle.dump(future_dist_input_dir, open(r'inputs\future_dist_input_dir.pkl', 'wb'))
        cPickle.dump(gcbm_raw_output_dir, open(r'inputs\gcbm_raw_output_dir.pkl', 'wb'))
        cPickle.dump(gcbm_configs_dir, open(r'inputs\gcbm_configs_dir.pkl', 'wb'))
        cPickle.dump(reportingIndicators, open(r'inputs\reportingIndicators.pkl', 'wb'))
        cPickle.dump(gcbm_exe, open(r'inputs\gcbm_exe.pkl', 'wb'))
        cPickle.dump(area_majority_rule, open(r'inputs\area_majority_rule.pkl', 'wb'))
        print "Done\n---------------------"
    except:
        print "Failed to save inputs."
        raise

def load_inputs():
    global inventory
    global historicFire1
    global historicFire2
    global historicHarvest
    global historicInsect
    global rollbackDisturbances
    global NAmat
    global spatialBoundaries
    global transitionRules
    global yieldTable
    global AIDB
    global resolution
    global rollback_enabled
    global historic_range
    global rollback_range
    global future_range
    global activity_start_year
    global inventory_raster_out
    global rollback_dist_out
    global tiler_scenarios
    global GCBM_scenarios
    global recliner2gcbm_config_dir
    global recliner2gcbm_output_path
    global recliner2gcbm_exe_path
    global tiler_output_dir
    global future_dist_input_dir
    global gcbm_raw_output_dir
    global gcbm_configs_dir
    global reportingIndicators
    global gcbm_exe
    global area_majority_rule
    try:
        print "----------------------\nLoading inputs...",
        logging.info('Loading inputs from {}'.format(os.path.join(os.getcwd(),'inputs')))
        inventory = cPickle.load(open(r'inputs\inventory.pkl'))
        historicFire1 = cPickle.load(open(r'inputs\historicFire1.pkl'))
        historicFire2 = cPickle.load(open(r'inputs\historicFire2.pkl'))
        historicHarvest = cPickle.load(open(r'inputs\historicHarvest.pkl'))
        historicInsect = cPickle.load(open(r'inputs\historicInsect.pkl'))
        rollbackDisturbances = cPickle.load(open(r'inputs\rollbackDisturbances.pkl'))
        NAmat = cPickle.load(open(r'inputs\NAmat.pkl'))
        spatialBoundaries = cPickle.load(open(r'inputs\spatialBoundaries.pkl'))
        transitionRules = cPickle.load(open(r'inputs\transitionRules.pkl'))
        yieldTable = cPickle.load(open(r'inputs\yieldTable.pkl'))
        AIDB = cPickle.load(open(r'inputs\AIDB.pkl'))
        resolution = cPickle.load(open(r'inputs\resolution.pkl'))
        rollback_enabled = cPickle.load(open(r'inputs\rollback_enabled.pkl'))
        historic_range = cPickle.load(open(r'inputs\historic_range.pkl'))
        rollback_range = cPickle.load(open(r'inputs\rollback_range.pkl'))
        future_range = cPickle.load(open(r'inputs\future_range.pkl'))
        activity_start_year = cPickle.load(open(r'inputs\activity_start_year.pkl'))
        inventory_raster_out = cPickle.load(open(r'inputs\inventory_raster_out.pkl'))
        tiler_scenarios = cPickle.load(open(r'inputs\tiler_scenarios.pkl'))
        GCBM_scenarios = cPickle.load(open(r'inputs\GCBM_scenarios.pkl'))
        tiler_output_dir = cPickle.load(open(r'inputs\tiler_output_dir.pkl'))
        recliner2gcbm_config_dir = cPickle.load(open(r'inputs\recliner2gcbm_config_dir.pkl'))
        recliner2gcbm_output_path = cPickle.load(open(r'inputs\recliner2gcbm_output_path.pkl'))
        recliner2gcbm_exe_path = cPickle.load(open(r'inputs\recliner2gcbm_exe_path.pkl'))
        future_dist_input_dir = cPickle.load(open(r'inputs\future_dist_input_dir.pkl'))
        gcbm_raw_output_dir = cPickle.load(open(r'inputs\gcbm_raw_output_dir.pkl'))
        gcbm_configs_dir = cPickle.load(open(r'inputs\gcbm_configs_dir.pkl'))
        reportingIndicators = cPickle.load(open(r'inputs\reportingIndicators.pkl'))
        gcbm_exe = cPickle.load(open(r'inputs\gcbm_exe.pkl'))
        area_majority_rule = cPickle.load(open(r'inputs\area_majority_rule.pkl'))
        logging.info('Loaded inputs.')
        print "Done\n----------------------"
    except:
        print "Failed to load inputs."
        raise

def save_objects():
    try:
        print 'Saving objects...',
        if not os.path.exists('objects'):
            os.mkdir('objects')
        cPickle.dump(inventory, open(r'objects\inventory.pkl', 'wb'))
        cPickle.dump(transitionRules, open(r'objects\transitionRules.pkl', 'wb'))
        cPickle.dump(yieldTable, open(r'objects\yieldTable.pkl', 'wb'))
        cPickle.dump(general_lyrs, open(r'objects\general_lyrs.pkl', 'wb'))
        print 'Done'
        logging.info('Objects Saved. Can restart from this point forward.')
    except:
        print "Failed to save objects."
        raise

def load_objects():
    global inventory
    global transitionRules
    global yieldTable
    global general_lyrs
    try:
        print 'Loading objects...',
        inventory = cPickle.load(open(r'objects\inventory.pkl'))
        transitionRules = cPickle.load(open(r'objects\transitionRules.pkl'))
        yieldTable = cPickle.load(open(r'objects\yieldTable.pkl'))
        general_lyrs = cPickle.load(open(r'objects\general_lyrs.pkl'))
        print 'Done'
        logging.info('Objects loaded.')
    except:
        print "Failed to load objects."
        raise

if __name__=="__main__":
    try:
        for flag in ("success", "failure"):
            if os.path.exists(flag):
                os.remove(flag)
                    
        sys.path.insert(0, '../../../03_tools/regional_preprocessing/gcbm_preprocessing')
        import preprocess_tools
        gridGeneration = __import__("01_grid_generation")
        rollback = __import__("02_rollback")
        tiler_imp = __import__("03_tiler")
        recliner2GCBM = __import__("04_recliner2GCBM")
        GCBMconfig = __import__("05_GCBM_config")

        # Logging
        debug_log = r'logs\DebugLogPreprocessor.log'
        if not os.path.exists(os.path.dirname(debug_log)):
            os.makedirs(os.path.dirname(debug_log))
        elif os.path.exists(debug_log):
            os.unlink(debug_log)
        logging.basicConfig(filename=debug_log, format='[%(asctime)s] %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%b%d %H:%M:%S')

        load_inputs()

        sb_base_percent = tiler_scenarios.itervalues().next()[0]

        ### Initialize function classes
        PP = preprocess_tools.progressprinter.ProgressPrinter()
        fishnet = gridGeneration.create_grid.Fishnet(inventory, resolution, PP)
        inventoryGridder = gridGeneration.grid_inventory.GridInventory(inventory, future_dist_input_dir, PP, area_majority_rule)
        mergeDist = rollback.merge_disturbances.MergeDisturbances(inventory, [historicFire1, historicFire2, historicHarvest], PP)
        intersect = rollback.intersect_disturbances_inventory.IntersectDisturbancesInventory(inventory, spatialBoundaries, rollback_range, PP)
        calcDistDEdiff = rollback.update_inventory.CalculateDistDEdifference(inventory, PP)
        calcNewDistYr = rollback.update_inventory.CalculateNewDistYr(inventory, rollback_range, historicHarvest.getYearField(), PP)
        updateInv = rollback.update_inventory.updateInvRollback(inventory, inventory_raster_out, rollbackDisturbances, rollback_range, resolution, sb_base_percent, reportingIndicators, PP)
        tiler = tiler_imp.tiler.Tiler(
            spatialBoundaries=spatialBoundaries,
            inventory=inventory,
            rollbackDisturbances=rollbackDisturbances,
            NAmat=NAmat,
            rollback_range=rollback_range, historic_range=historic_range, future_range=future_range,activity_start_year=activity_start_year,
            resolution=resolution, ProgressPrinter=PP
        )
        projDistGenerator = tiler_imp.projected_disturbances_placeholder.ProjectedDisturbancesPlaceholder(inventory, rollbackDisturbances,
            future_range, rollback_range, activity_start_year, PP)
        r2GCBM = recliner2GCBM.recliner2GCBM.Recliner2GCBM(config_dir=recliner2gcbm_config_dir, output_path=recliner2gcbm_output_path,
            transitionRules=transitionRules,yieldTable=yieldTable,aidb=AIDB,ProgressPrinter=PP, exe_path=recliner2gcbm_exe_path)
        gcbmConfigurer = GCBMconfig.configure_gcbm.ConfigureGCBM(output_dir=gcbm_raw_output_dir, gcbm_configs_dir=gcbm_configs_dir,
            GCBM_scenarios=GCBM_scenarios, base_scenario='Base', inventory=inventory, reportingIndicators=reportingIndicators,
            resolution=resolution,rollback_range=rollback_range,actv_start_year=activity_start_year,future_range=future_range,ProgressPrinter=PP)

        general_lyrs = None

        ### Execute Functions

        # -- Grid generation
        fishnet.createFishnet()

        # -- Grid inventory
        inventoryGridder.gridInventory()

        if not rollback_enabled: # ***
            inventoryGridder.exportInventory(inventory_raster_out, resolution) # ***

        else: # ***
            # -- Start of rollback
            mergeDist.runMergeDisturbances()
            intersect.runIntersectDisturbancesInventory()
            calcDistDEdiff.calculateDistDEdifference()
            calcNewDistYr.calculateNewDistYr()
            updateInv.updateInvRollback()  # ***
            # -- End of rollback

        # -- Configure Tiler
        general_lyrs = configure_tiler()

        ## -- Run Tiler for each scenario
        tiler_order = ["Base"] + [scen for scen in tiler_scenarios.keys() if scen.lower() != "base"]
        for i, scenario_name in enumerate(tiler_order, 1):
            write_transition_rules = i == len(tiler_scenarios) # only write transition rules after they've all been collected
            tiler.processProjectedDisturbances(scenario_name, tiler_scenarios[scenario_name])
            transitionRules = tiler.runTiler(tiler_output_dir, scenario_name, write_transition_rules)

        # -- Prep and run recliner2GCBM
        r2GCBM.prepTransitionRules(transitionRules) # ***
        r2GCBM.prepYieldTable(yieldTable)
        r2GCBM.runRecliner2GCBM() # ***

        # -- Configure GCBM
        gcbmConfigurer.configureGCBM(recliner2gcbm_output_path, general_lyrs, tiler_output_dir) # ***

        # Create success flag file that other tools can check for.
        with open("success", "w"): pass
    except:
        # Create failure flag file that other tools can check for.
        with open("failure", "w"): pass
        raise
